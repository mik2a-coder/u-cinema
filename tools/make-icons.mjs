/* Génère les icônes (favicon, écran d'accueil, aperçu de lien) à partir de img/logo-mark3.png.
   Usage : python3 -m http.server 8731 (dans le dossier du projet) puis node tools/make-icons.mjs */
import {spawn} from 'node:child_process';import fs from 'node:fs';
const ch=spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',['--headless=new','--remote-debugging-port=9341','--user-data-dir=/tmp/ico'+Date.now(),'about:blank'],{stdio:'ignore'});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
let tabs;for(let i=0;i<40;i++){try{tabs=await (await fetch('http://127.0.0.1:9341/json')).json();if(tabs.length)break}catch(e){}await sleep(250)}
const ws=new WebSocket(tabs.find(t=>t.type==='page').webSocketDebuggerUrl);await new Promise(r=>ws.onopen=r);
let id=0;const pend={};ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&pend[m.id]){pend[m.id](m.result);delete pend[m.id]}};
const send=(method,params={})=>new Promise(r=>{const i=++id;pend[i]=r;ws.send(JSON.stringify({id:i,method,params}))});
await send('Page.enable');await send('Page.navigate',{url:'http://localhost:8731/manifest.webmanifest'});await sleep(1200);
const js=`(async()=>{const img=new Image();img.src='/img/logo-mark3.png';await img.decode();
 const mk=(w,h,bg,k,round)=>{const c=document.createElement('canvas');c.width=w;c.height=h;const x=c.getContext('2d');x.imageSmoothingQuality='high';
  if(bg){x.fillStyle=bg;if(round){x.beginPath();x.roundRect(0,0,w,h,round);x.fill()}else x.fillRect(0,0,w,h)}
  const s=Math.min(w,h)*k;x.drawImage(img,(w-s)/2,(h-s)/2,s,s);return c.toDataURL('image/png')};
 return {f32:mk(32,32,null,1),f48:mk(48,48,null,1),a180:mk(180,180,'#F7F2E8',.82),i192:mk(192,192,'#F7F2E8',.82,40),i512:mk(512,512,'#F7F2E8',.82,110),m512:mk(512,512,'#F7F2E8',.6)}})()`;
const r=await send('Runtime.evaluate',{expression:js,awaitPromise:true,returnByValue:true});
const o=r.result.value,w=(n,d)=>fs.writeFileSync('icons/'+n,Buffer.from(d.split(',')[1],'base64'));
w('favicon-32.png',o.f32);w('favicon-48.png',o.f48);w('apple-touch-icon.png',o.a180);w('icon-192.png',o.i192);w('icon-512.png',o.i512);w('icon-512-maskable.png',o.m512);
ws.close();ch.kill();console.log('icônes générées');process.exit(0)
