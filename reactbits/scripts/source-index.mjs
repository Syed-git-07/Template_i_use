// Facts and source locations only. Restricted implementation code stays local.
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath,pathToFileURL } from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const commit='d01aa914dcbe76da8b2923ebf872b5c8b1066e4c';
const snapshot=process.argv[2]||path.resolve(root,'../.local/react-bits',commit);
const {default:ts}=await import(pathToFileURL(path.resolve(root,'../.local/tooling/node_modules/typescript/lib/typescript.js')));
const {readSourceDefaults,auditPropDocs}=await import(pathToFileURL(path.join(snapshot,'scripts/checkPropDocs.js')));
const catalogue=JSON.parse(fs.readFileSync(path.join(root,'catalogue/index.json'),'utf8'));
const variants=['content','tailwind','ts-default','ts-tailwind'];
const normalize=s=>s.replace(/[^a-z0-9]/gi,'').toLowerCase();
const sourceUrl=file=>`https://github.com/DavidHDev/react-bits/blob/${commit}/${file}`;
const scalar=node=>!node?undefined:ts.isStringLiteral(node)?node.text:ts.isNumericLiteral(node)?Number(node.text):node.kind===ts.SyntaxKind.TrueKeyword?true:node.kind===ts.SyntaxKind.FalseKeyword?false:undefined;
const walk=(node,visit)=>{visit(node);ts.forEachChild(node,c=>walk(c,visit));};
const rows=[];const manifest={};
for(const category of fs.readdirSync(path.join(snapshot,'src/content')).sort()){
 for(const name of fs.readdirSync(path.join(snapshot,'src/content',category)).sort()){
  const primary=path.join(snapshot,'src/content',category,name,`${name}.jsx`);
  if(!fs.existsSync(primary))continue;
  const entry=catalogue.items.find(x=>x.kind==='component'&&normalize(x.slug)===normalize(name));
  const row={name,category,slug:entry?.slug||null,url:entry?.url||null,publicly_listed:!!entry,variants:[],props:[],states:[],events:[],motion:[],dependencies:[],signals:{}};
  for(const variant of variants){
   const relative=`src/${variant}/${category}/${name}/${name}.${variant.startsWith('ts-')?'tsx':'jsx'}`;
   const file=path.join(snapshot,relative);const content=fs.readFileSync(file,'utf8');
   const defaults=Object.fromEntries(readSourceDefaults(file,name));
   const sha256=crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');
   row.variants.push({variant,file:relative,url:sourceUrl(relative),sha256,scalar_defaults:defaults});manifest[relative]=sha256;
   // The canonical JS+CSS variant is used for structural locations; all four defaults are retained above.
   if(variant!=='content')continue;
   const ast=ts.createSourceFile(file,content,ts.ScriptTarget.Latest,true,ts.ScriptKind.JSX);
   const line=node=>ast.getLineAndCharacterOfPosition(node.getStart(ast)).line+1;
   walk(ast,node=>{
    if(ts.isImportDeclaration(node)&&ts.isStringLiteral(node.moduleSpecifier)&&!node.moduleSpecifier.text.startsWith('.'))row.dependencies.push(node.moduleSpecifier.text);
    if(ts.isJsxAttribute(node)&&/^on[A-Z]/.test(node.name.getText(ast)))row.events.push({name:node.name.getText(ast),line:line(node)});
    if(ts.isCallExpression(node)&&/addEventListener$/.test(node.expression.getText(ast))&&typeof scalar(node.arguments[0])==='string')row.events.push({name:scalar(node.arguments[0]),line:line(node)});
    if(ts.isCallExpression(node)&&/^set[A-Z]/.test(node.expression.getText(ast))){const value=scalar(node.arguments[0]);if(typeof value==='string'&&value.length<50)row.states.push({setter:node.expression.getText(ast),value,line:line(node)});}
    if(ts.isPropertyAssignment(node)&&/^(stiffness|damping|mass|duration|delay|bounce|dragElastic|dragMomentum|ease|restSpeed|restDelta|velocity|friction|threshold)$/.test(node.name.getText(ast))){
     const value=scalar(node.initializer);row.motion.push({parameter:node.name.getText(ast),line:line(node),...(value===undefined?{computed:true}:{value})});
    }
   });
   for(const [key,regex] of Object.entries({reduced_motion:/prefers-reduced-motion|useReducedMotion/,keyboard:/onKeyDown|onKeyUp|keydown/,pointer_cancel:/pointercancel|onPointerCancel/,visibility:/IntersectionObserver|document\.hidden|visibilitychange/,cleanup:/cancelAnimationFrame|removeEventListener|\.dispose\(/,frame_loop:/requestAnimationFrame|useFrame/,microphone:/getUserMedia|MediaRecorder/,network:/\bfetch\(|XMLHttpRequest|axios\./,webgl:/WebGL|THREE|WebGLRenderer|\bRenderer\b/,resize:/ResizeObserver|resize/}))row.signals[key]=regex.test(content);
   row.dependencies=[...new Set(row.dependencies)];
   const css=relative.replace(/\.jsx$/,'.css');if(fs.existsSync(path.join(snapshot,css))){row.css={file:css,url:sourceUrl(css),motion_lines:[]};const bytes=fs.readFileSync(path.join(snapshot,css));manifest[css]=crypto.createHash('sha256').update(bytes).digest('hex');bytes.toString('utf8').split(/\r?\n/).forEach((s,i)=>{if(/transition|animation|@keyframes|prefers-reduced-motion/.test(s))row.css.motion_lines.push(i+1);});}
  }
  const demoRelative=`src/demo/${category}/${name}Demo.jsx`;const demo=path.join(snapshot,demoRelative);
  if(fs.existsSync(demo)){
   row.demo_url=sourceUrl(demoRelative);const ast=ts.createSourceFile(demo,fs.readFileSync(demo,'utf8'),ts.ScriptTarget.Latest,true,ts.ScriptKind.JSX);
   walk(ast,node=>{
    if(!ts.isObjectLiteralExpression(node))return;
    const values={};for(const p of node.properties)if(ts.isPropertyAssignment(p))values[p.name.getText(ast).replace(/['"]/g,'')]=scalar(p.initializer);
    if(typeof values.name==='string'&&typeof values.type==='string'&&values.default!==undefined){row.props.push({name:values.name,type:values.type,documented_default:values.default,line:ast.getLineAndCharacterOfPosition(node.getStart(ast)).line+1});}
   });
  }
  rows.push(row);
 }
}
const audit=auditPropDocs(snapshot);
const cleanAudit={...audit,errors:audit.errors.map(e=>({kind:e.kind,component:e.component,prop:e.prop,actual:e.actual,documented:e.documented,values:e.values}))};
const allFiles=(dir)=>fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?allFiles(path.join(dir,e.name)):[path.join(dir,e.name)]);
for(const relRoot of ['src','scripts'])for(const file of allFiles(path.join(snapshot,relRoot))){const relative=path.relative(snapshot,file).replaceAll('\\','/');manifest[relative]=crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');}
const out=path.join(root,'catalogue');fs.mkdirSync(path.join(root,'components'),{recursive:true});
fs.writeFileSync(path.join(out,'source-index.json'),JSON.stringify({commit,license:'MIT + Commons Clause; no component-library redistribution',note:'Factual APIs, parameters and pinned source locations; no implementation bodies. Structural signals are not behavior certifications.',items:rows},null,2));
fs.writeFileSync(path.join(out,'source-audit.json'),JSON.stringify(cleanAudit,null,2));
fs.writeFileSync(path.join(out,'local-source-sha256.json'),JSON.stringify(manifest,null,2));
const escape=s=>String(s??'—').replaceAll('|','\\|').replaceAll('\n',' ');
for(const r of rows){
 const lines=[`# ${r.name}`,'',`Category: ${r.category}. Public entry: ${r.url?`[${r.name}](${r.url})`:'not present in the current public catalogue'}.`,'',`Source pinned to \`${commit}\`. Full implementation stays in the excluded local snapshot; links below open the original source.`,'','## Variants','',...r.variants.map(v=>`- [${v.variant}](${v.url})`),'','## API facts','','| Prop | Type | Documented default | Source scalar default |','| --- | --- | --- | --- |'];
 for(const p of r.props)lines.push(`| ${escape(p.name)} | ${escape(p.type)} | ${escape(p.documented_default)} | ${escape(r.variants[0].scalar_defaults[p.name])} |`);
 lines.push('','Object/function defaults are intentionally not flattened; follow the original source. The global source audit checks comparable scalar defaults across all four variants.','',`Dependencies: ${r.dependencies.join(', ')||'No external import found in canonical component.'}`,'','## Interaction locations','');
 for(const e of r.events)lines.push(`- [${e.name}, line ${e.line}](${r.variants[0].url}#L${e.line})`);
 lines.push('','## Motion locations','');
 for(const m of r.motion)lines.push(`- [${m.parameter}, line ${m.line}](${r.variants[0].url}#L${m.line}): ${m.computed?'computed; read the linked expression':JSON.stringify(m.value)}`);
 if(r.css)lines.push('',`[Stylesheet](${r.css.url}); motion-related lines: ${r.css.motion_lines.join(', ')||'none matched'}.`);
 lines.push('','## Observed source structure','',`Literal state assignments: ${r.states.map(s=>`${s.setter} → ${s.value} (line ${s.line})`).join('; ')||'none captured by the structural index'}.`,'',`Signals present: ${Object.entries(r.signals).filter(([,v])=>v).map(([k])=>k).join(', ')||'none matched'}.`,'','These are source facts and search locations, not an exhaustive semantic audit. Computed state paths, physics, interruption behavior and CSS need the original implementation. See the browser survey and gesture report for runtime evidence.','');
 fs.writeFileSync(path.join(root,'components',`${r.name}.md`),lines.join('\n'));
}
console.log(JSON.stringify({components:rows.length,public:rows.filter(r=>r.publicly_listed).length,unlisted:rows.filter(r=>!r.publicly_listed).map(r=>r.name),variants:rows.reduce((a,r)=>a+r.variants.length,0),sourceFiles:Object.keys(manifest).length,audit:{...cleanAudit,errors:cleanAudit.errors.length}},null,2));
