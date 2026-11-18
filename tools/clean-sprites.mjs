/* Nettoie les 11 poses du chat (img/chat/raw01..11.png) : fond blanc -> transparent, rognage. Sortie : img/chat/c01..c11.png
   Usage : python3 -m http.server 8731 puis node tools/clean-sprites.mjs */
import {spawn} from 'node:child_process';import fs from 'node:fs';
const ch=spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',['--headless=new','--remote-debugging-port=9347','--user-data-dir=/tmp/cl'+Date.now(),'about:blank'],{stdio:'ignore'});
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
let tabs;for(let i=0;i<40;i++){try{tabs=await (await fetch('http://127.0.0.1:9347/json')).json();if(tabs.length)break}catch(e){}await sleep(250)}
const ws=new WebSocket(tabs.find(t=>t.type==='page').webSocketDebuggerUrl);await new Promise(r=>ws.onopen=r);
let id=0;const pend={};ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id&&pend[m.id]){pend[m.id](m.result);delete pend[m.id]}};
const send=(method,params={})=>new Promise(r=>{const i=++id;pend[i]=r;ws.send(JSON.stringify({id:i,method,params}))});
await send('Page.enable');await send('Page.navigate',{url:'http://localhost:8731/manifest.webmanifest'});await sleep(1000);
const js=`(async()=>{const matte=(p,w,h)=>{const bg=new Uint8Array(w*h),st=[];const test=i=>{const o=i*4,mn=Math.min(p[o],p[o+1],p[o+2]),sat=Math.max(p[o],p[o+1],p[o+2])-mn;return mn>215&&sat<50};
 const push=i=>{if(!bg[i]&&test(i)){bg[i]=1;st.push(i)}};
 for(let x=0;x<w;x++){push(x);push((h-1)*w+x)}for(let y=0;y<h;y++){push(y*w);push(y*w+w-1)}
 while(st.length){const i=st.pop(),x=i%w,y=(i/w)|0;if(x>0)push(i-1);if(x<w-1)push(i+1);if(y>0)push(i-w);if(y<h-1)push(i+w)}
 for(let i=0;i<w*h;i++){const o=i*4,mn=Math.min(p[o],p[o+1],p[o+2]),sat=Math.max(p[o],p[o+1],p[o+2])-mn;if(mn>=250&&sat<8)bg[i]=1}
 /* liseré : on ronge 2 pixels clairs au contact du fond pour supprimer le halo blanc */
 for(let pass=0;pass<2;pass++){const add=[];for(let i=0;i<w*h;i++){if(bg[i])continue;const x=i%w,y=(i/w)|0;if(!((x>0&&bg[i-1])||(x<w-1&&bg[i+1])||(y>0&&bg[i-w])||(y<h-1&&bg[i+w])))continue;const o=i*4,mn=Math.min(p[o],p[o+1],p[o+2]);if(mn>185)add.push(i)}add.forEach(i=>bg[i]=1)}
 for(let i=0;i<w*h;i++)if(bg[i])p[i*4+3]=0;
 /* bord adouci : alpha réduit au contact du fond */
 for(let i=0;i<w*h;i++){if(bg[i])continue;const x=i%w,y=(i/w)|0;if((x>0&&bg[i-1])||(x<w-1&&bg[i+1])||(y>0&&bg[i-w])||(y<h-1&&bg[i+w]))p[i*4+3]=170}};const out={};for(let n=1;n<=11;n++){const k=String(n).padStart(2,'0');
 const im=await new Promise(r=>{const i=new Image();i.onload=()=>r(i);i.src='/img/chat/raw'+k+'.png'});
 const w=im.naturalWidth,h=im.naturalHeight,c=document.createElement('canvas');c.width=w;c.height=h;const g=c.getContext('2d',{willReadFrequently:true});g.drawImage(im,0,0);
 const d=g.getImageData(0,0,w,h),p=d.data;
 matte(p,w,h);
 g.putImageData(d,0,0);
 let x0=w,y0=h,x1=0,y1=0;for(let y=0;y<h;y++)for(let x=0;x<w;x++)if(p[(y*w+x)*4+3]>60){if(x<x0)x0=x;if(x>x1)x1=x;if(y<y0)y0=y;if(y>y1)y1=y}
 const cw=x1-x0+1,chh=y1-y0+1,o=document.createElement('canvas');o.width=cw;o.height=chh;o.getContext('2d').drawImage(c,x0,y0,cw,chh,0,0,cw,chh);out[k]=[o.toDataURL('image/png'),cw,chh]}
 return out})()`;
const r=await send('Runtime.evaluate',{expression:js,awaitPromise:true,returnByValue:true});
if(r.exceptionDetails)console.log(JSON.stringify(r.exceptionDetails).slice(0,400));
for(const [k,[d,w,h]] of Object.entries(r.result.value)){fs.writeFileSync('img/chat/c'+k+'.png',Buffer.from(d.split(',')[1],'base64'));console.log('c'+k,w,h)}
ws.close();ch.kill();process.exit(0)
