/* Captures d'écran automatiques du prototype (Chrome sans interface).
   Usage : node tools/shoot.mjs <largeur> <hauteur> <préfixe-de-fichier> <scénario.json> [url]
   Le scénario est une liste d'étapes {js, wait, shot} exécutées dans la page. */
import {spawn} from 'node:child_process';import fs from 'node:fs';
const [W,H,out,file,url]=[+process.argv[2],+process.argv[3],process.argv[4],process.argv[5],process.argv[6]||'http://localhost:8731/index.html#nodev:0:novid,novt'];
const steps=JSON.parse(fs.readFileSync(file,'utf8'));
const ch=spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',['--headless=new','--remote-debugging-port=9337','--user-data-dir=/tmp/shoot'+Date.now(),'--window-size='+W+','+H,'--hide-scrollbars','about:blank'],{stdio:'ignore'});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
let tabs;for(let i=0;i<40;i++){try{tabs=await (await fetch('http://127.0.0.1:9337/json')).json();if(tabs.length)break}catch(e){}await sleep(250)}
const ws=new WebSocket(tabs.find(t=>t.type==='page').webSocketDebuggerUrl);await new Promise(r=>ws.onopen=r);
let id=0;const pend={};ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&pend[m.id]){pend[m.id](m.result);delete pend[m.id]}};
const send=(method,params={})=>new Promise(r=>{const i=++id;pend[i]=r;ws.send(JSON.stringify({id:i,method,params}))});
await send('Emulation.setDeviceMetricsOverride',{width:W,height:H,deviceScaleFactor:1,mobile:W<600});
await send('Page.enable');await send('Runtime.enable');await send('Page.navigate',{url});await sleep(2500);
const ev=async x=>{const r=await send('Runtime.evaluate',{expression:x,awaitPromise:true,returnByValue:true});if(r.exceptionDetails)console.log('ERR',JSON.stringify(r.exceptionDetails).slice(0,300));return r.result&&r.result.value};
for(const s of steps){if(s.js){const v=await ev(s.js);if(v!==1&&v!==undefined)console.log(typeof v==='string'?v:JSON.stringify(v))}if(s.wait)await sleep(s.wait);if(s.shot){const r=await send('Page.captureScreenshot',{format:'jpeg',quality:72});fs.writeFileSync(`${out}_${s.shot}.jpg`,Buffer.from(r.data,'base64'))}}
ws.close();ch.kill();process.exit(0)
