// Extract factual source locations and API structure, without publishing implementations.
import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';import {execFileSync} from 'node:child_process';import {fileURLToPath,pathToFileURL} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const ts=(await import(pathToFileURL(path.join(root,'.local/tooling/node_modules/typescript/lib/typescript.js')).href)).default;
const config={
 shadcn:{repo:'shadcn-ui/ui',dirs:['apps/v4/registry','apps/v4/content','apps/v4/lib','apps/v4/hooks','apps/v4/styles','packages']},
 'motion-primitives':{repo:'ibelick/motion-primitives',dirs:['components/core','components/ui','app/docs','hooks']},
 cult:{repo:'nolly-studio/cult-ui',dirs:['apps/www/registry','apps/www/content','apps/www/styles']},
 interior:{repo:'ddoemonn/interior',dirs:['components','lib','app']},aceternity:{dirs:['components']}
};
const scalar=n=>{if(!n)return undefined;if(ts.isStringLiteral(n)||ts.isNoSubstitutionTemplateLiteral(n))return n.text;if(ts.isNumericLiteral(n))return Number(n.text);if(n.kind===ts.SyntaxKind.TrueKeyword)return true;if(n.kind===ts.SyntaxKind.FalseKeyword)return false;if(n.kind===ts.SyntaxKind.NullKeyword)return null;if(ts.isPrefixUnaryExpression(n)&&n.operator===ts.SyntaxKind.MinusToken&&ts.isNumericLiteral(n.operand))return -Number(n.operand.text);};
function walk(n,fn){fn(n);ts.forEachChild(n,c=>walk(c,fn));}
function files(dir){return fs.existsSync(dir)?fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?files(path.join(dir,e.name)):[path.join(dir,e.name)]):[];}
for(const site of process.argv.slice(2)){
 const cfg=config[site],local=path.join(root,'.local/upstream',site),commit=cfg.repo?execFileSync('git',['rev-parse','HEAD'],{cwd:local,encoding:'utf8'}).trim():null;
 const list=cfg.dirs.flatMap(d=>files(path.join(local,d))).filter(f=>/\.(tsx?|jsx?|css|mdx)$/.test(f));const rows=[];
 for(const f of list){
  const rel=path.relative(local,f).replaceAll('\\','/'),bytes=fs.readFileSync(f),text=bytes.toString('utf8'),lines=text.split(/\r?\n/);
  const row={file:rel,sha256:crypto.createHash('sha256').update(bytes).digest('hex'),lines:lines.length,url:cfg.repo?`https://github.com/${cfg.repo}/blob/${commit}/${rel}`:null,imports:[],exports:[],props:[],defaults:[],motion:[],events:[],styles:[],signals:{}};
  if(/\.[jt]sx?$/.test(f)){
   const ast=ts.createSourceFile(f,text,ts.ScriptTarget.Latest,true,/[jt]sx$/.test(f)?ts.ScriptKind.TSX:ts.ScriptKind.TS);const line=n=>ast.getLineAndCharacterOfPosition(n.getStart(ast)).line+1;
   walk(ast,n=>{
    if(ts.isImportDeclaration(n)&&n.moduleSpecifier)row.imports.push(n.moduleSpecifier.text);
    if((ts.isFunctionDeclaration(n)||ts.isInterfaceDeclaration(n)||ts.isTypeAliasDeclaration(n))&&n.name)row.exports.push({name:n.name.text,kind:ts.SyntaxKind[n.kind],line:line(n)});
    if(ts.isPropertySignature(n)&&n.name)row.props.push({name:n.name.getText(ast),type:n.type?.getText(ast),optional:!!n.questionToken,line:line(n)});
    if(ts.isBindingElement(n)&&n.initializer){const value=scalar(n.initializer);if(value!==undefined)row.defaults.push({name:n.name.getText(ast),value,line:line(n)});}
    if(ts.isJsxAttribute(n)&&/^on[A-Z]/.test(n.name.getText(ast)))row.events.push({name:n.name.getText(ast),line:line(n)});
    if(ts.isCallExpression(n)&&ts.isPropertyAccessExpression(n.expression)&&n.expression.name.text==='addEventListener')row.events.push({name:scalar(n.arguments[0])??'computed event',line:line(n)});
    if(ts.isPropertyAssignment(n)&&/^(stiffness|damping|mass|duration|delay|bounce|ease|dragElastic|dragMomentum|threshold|restSpeed|restDelta)$/.test(n.name.getText(ast).replaceAll("'",''))){const value=scalar(n.initializer);row.motion.push({parameter:n.name.getText(ast),line:line(n),...(value===undefined?{computed:true}:{value})});}
   });
  }
  for(const [i,line] of lines.entries())if(/font-family|fontFamily|@font-face|transition:|animation:|@keyframes|prefers-reduced-motion|--radius|--background|--foreground/.test(line))row.styles.push({line:i+1,kind:/font/.test(line)?'typography':'style/motion'});
  for(const [key,regex] of Object.entries({reduced_motion:/prefers-reduced-motion|useReducedMotion/,keyboard:/onKeyDown|onKeyUp|keydown/,pointer_cancel:/pointercancel|onPointerCancel/,focus:/FocusScope|FocusTrap|focus\(|onFocus|onBlur/,cleanup:/cancelAnimationFrame|removeEventListener|\.dispose\(/,async:/\basync\b|Promise|fetch\(/,resize:/ResizeObserver/,visibility:/IntersectionObserver|visibilitychange/,aria:/aria-|role=/}))row.signals[key]=regex.test(text);
  rows.push(row);
 }
 const out=path.join(root,site,'catalogue');fs.mkdirSync(out,{recursive:true});fs.writeFileSync(path.join(out,'source-index.json'),JSON.stringify({commit,repository:cfg.repo?`https://github.com/${cfg.repo}`:null,local_snapshot:`.local/upstream/${site}`,note:'Factual structural index, not exhaustive semantic verification. All implementation stays local; originals linked where available.',items:rows},null,2));
 console.log(site,commit,rows.length,'source/doc files');
}
