// Static metadata extraction only; upstream modules are never executed.
import fs from 'node:fs';import path from 'node:path';import {fileURLToPath,pathToFileURL} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');const ts=(await import(pathToFileURL(path.join(root,'.local/tooling/node_modules/typescript/lib/typescript.js')).href)).default;
const local=path.join(root,'.local/upstream/interior');
function val(n){if(!n)return undefined;if(ts.isStringLiteral(n)||ts.isNoSubstitutionTemplateLiteral(n))return n.text;if(ts.isNumericLiteral(n))return +n.text;if(ts.isArrayLiteralExpression(n))return n.elements.map(val);if(ts.isObjectLiteralExpression(n)){const o={};for(const p of n.properties)if(ts.isPropertyAssignment(p))o[p.name.getText().replace(/^['"]|['"]$/g,'')]=val(p.initializer);return o;}}
function variable(file,name){const ast=ts.createSourceFile(file,fs.readFileSync(path.join(local,file),'utf8'),ts.ScriptTarget.Latest,true);let found;function visit(n){if(ts.isVariableDeclaration(n)&&n.name.getText(ast)===name)found=val(n.initializer);ts.forEachChild(n,visit);}visit(ast);return found;}
const meta={...variable('lib/registry.generated.ts','generated'),...variable('lib/registry.meta.ts','handAuthored')};const rows=variable('lib/registry.ts','seeds').flatMap(([id,category,entries])=>entries.map(([number,slug,name])=>({number,category,slug,name,...meta[slug]})));
for(const r of rows)delete r.usage;
fs.mkdirSync(path.join(root,'interior/catalogue'),{recursive:true});fs.copyFileSync(path.join(local,'LICENSE'),path.join(root,'interior/UPSTREAM-LICENSE.txt'));
fs.writeFileSync(path.join(root,'interior/catalogue/contracts.json'),JSON.stringify({attribution:'API notes and behavior contracts by ozzy / interior.dev, MIT licensed; see UPSTREAM-LICENSE.txt. Upstream claims, not independently tested guarantees.',items:rows},null,2));
console.log(rows.length,'Interior metadata contracts');
