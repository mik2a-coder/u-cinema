/* Découpe les poses du chat (planches img/chat/sheet-*.webp) en images transparentes pour le mini-jeu.
   Usage : python3 -m http.server 8731 puis node tools/cut-chat.mjs */
import {spawn} from 'node:child_process';import fs from 'node:fs';
const ch=spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',['--headless=new','--remote-debugging-port=9343','--user-data-dir=/tmp/cut'+Date.now(),'about:blank'],{stdio:'ignore'});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
let tabs;for(let i=0;i<40;i++){try{tabs=await (await fetch('http://127.0.0.1:9343/json')).json();if(tabs.length)break}catch(e){}await sleep(250)}
const ws=new WebSocket(tabs.find(t=>t.type==='page').webSocketDebuggerUrl);await new Promise(r=>ws.onopen=r);
let id=0;const pend={};ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&pend[m.id]){pend[m.id](m.result);delete pend[m.id]}};
const send=(method,params={})=>new Promise(r=>{const i=++id;pend[i]=r;ws.send(JSON.stringify({id:i,method,params}))});
await send('Page.enable');await send('Page.navigate',{url:'http://localhost:8731/manifest.webmanifest'});await sleep(1000);
const FR=JSON.parse(process.argv[2]||'[]');
const js=`(async()=>{const L=src=>new Promise(r=>{const i=new Image();i.onload=()=>r(i);i.src=src});
 const A=await L('/img/chat/sheet-poses.webp'),B=await L('/img/chat/sheet-ref.webp');
 const out={size:[A.naturalWidth,A.naturalHeight,B.naturalWidth,B.naturalHeight]};
 for(const [name,sh,x,y,w,h] of ${JSON.stringify(FR)}){const im=sh==='A'?A:B;const c=document.createElement('canvas');c.width=w;c.height=h;const g=c.getContext('2d',{willReadFrequently:true});g.drawImage(im,x,y,w,h,0,0,w,h);
  const d=g.getImageData(0,0,w,h),p=d.data;
  // fond blanc -> transparent (progressif), puis rognage
  for(let i=0;i<p.length;i+=4){const r=p[i],gg=p[i+1],b=p[i+2],mn=Math.min(r,gg,b),sat=Math.max(r,gg,b)-mn;
   if(mn>236&&sat<26)p[i+3]=0;else if(mn>205&&sat<40)p[i+3]=Math.max(0,Math.min(255,(236-mn)*8))}
  g.putImageData(d,0,0);
  let x0=w,y0=h,x1=0,y1=0;for(let yy=0;yy<h;yy++)for(let xx=0;xx<w;xx++)if(p[(yy*w+xx)*4+3]>40){if(xx<x0)x0=xx;if(xx>x1)x1=xx;if(yy<y0)y0=yy;if(yy>y1)y1=yy}
  const cw=x1-x0+1,chh=y1-y0+1,o=document.createElement('canvas');o.width=cw;o.height=chh;o.getContext('2d').drawImage(c,x0,y0,cw,chh,0,0,cw,chh);out[name]=o.toDataURL('image/png')}
 return out})()`;
const r=await send('Runtime.evaluate',{expression:js,awaitPromise:true,returnByValue:true});
const o=r.result.value;console.log('tailles',o.size);
for(const k of Object.keys(o)){if(k==='size')continue;fs.writeFileSync('img/chat/'+k+'.png',Buffer.from(o[k].split(',')[1],'base64'))}
ws.close();ch.kill();process.exit(0)
