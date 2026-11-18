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
const js=`(async()=>{const matte=(p,w,h,noG)=>{const bg=new Uint8Array(w*h),st=[];const test=i=>{const o=i*4,mn=Math.min(p[o],p[o+1],p[o+2]),sat=Math.max(p[o],p[o+1],p[o+2])-mn;return mn>215&&sat<50};
 const push=i=>{if(!bg[i]&&test(i)){bg[i]=1;st.push(i)}};
 for(let x=0;x<w;x++){push(x);push((h-1)*w+x)}for(let y=0;y<h;y++){push(y*w);push(y*w+w-1)}
 while(st.length){const i=st.pop(),x=i%w,y=(i/w)|0;if(x>0)push(i-1);if(x<w-1)push(i+1);if(y>0)push(i-w);if(y<h-1)push(i+w)}
 if(!noG)for(let i=0;i<w*h;i++){const o=i*4,mn=Math.min(p[o],p[o+1],p[o+2]),sat=Math.max(p[o],p[o+1],p[o+2])-mn;if(mn>=250&&sat<8)bg[i]=1}
 /* liseré : on ronge 2 pixels clairs au contact du fond pour supprimer le halo blanc */
 for(let pass=0;pass<2;pass++){const add=[];for(let i=0;i<w*h;i++){if(bg[i])continue;const x=i%w,y=(i/w)|0;if(!((x>0&&bg[i-1])||(x<w-1&&bg[i+1])||(y>0&&bg[i-w])||(y<h-1&&bg[i+w])))continue;const o=i*4,mn=Math.min(p[o],p[o+1],p[o+2]);if(mn>185)add.push(i)}add.forEach(i=>bg[i]=1)}
 for(let i=0;i<w*h;i++)if(bg[i])p[i*4+3]=0;
 /* bord adouci : alpha réduit au contact du fond */
 for(let i=0;i<w*h;i++){if(bg[i])continue;const x=i%w,y=(i/w)|0;if((x>0&&bg[i-1])||(x<w-1&&bg[i+1])||(y>0&&bg[i-w])||(y<h-1&&bg[i+w]))p[i*4+3]=170}};const L=src=>new Promise(r=>{const i=new Image();i.onload=()=>r(i);i.src=src});
 const A=await L('/img/chat/sheet-poses.webp'),B=await L('/img/chat/sheet-ref.webp'),C=await L('/img/chat/sheet-sprites.webp');
 const out={size:[C.naturalWidth,C.naturalHeight]};
 for(const [name,sh,x,y,w,h,noG] of ${JSON.stringify(FR)}){const im=sh==='A'?A:sh==='B'?B:C;const c=document.createElement('canvas');c.width=w;c.height=h;const g=c.getContext('2d',{willReadFrequently:true});g.drawImage(im,x,y,w,h,0,0,w,h);
  const d=g.getImageData(0,0,w,h),p=d.data;
  matte(p,w,h,noG);
  g.putImageData(d,0,0);
  let x0=w,y0=h,x1=0,y1=0;for(let yy=0;yy<h;yy++)for(let xx=0;xx<w;xx++)if(p[(yy*w+xx)*4+3]>40){if(xx<x0)x0=xx;if(xx>x1)x1=xx;if(yy<y0)y0=yy;if(yy>y1)y1=yy}
  const cw=x1-x0+1,chh=y1-y0+1,o=document.createElement('canvas');o.width=cw;o.height=chh;o.getContext('2d').drawImage(c,x0,y0,cw,chh,0,0,cw,chh);out[name]=o.toDataURL('image/png')}
 return out})()`;
const r=await send('Runtime.evaluate',{expression:js,awaitPromise:true,returnByValue:true});
const o=r.result.value;console.log('tailles',o.size);
for(const k of Object.keys(o)){if(k==='size')continue;fs.writeFileSync('img/chat/'+k+'.png',Buffer.from(o[k].split(',')[1],'base64'))}
ws.close();ch.kill();process.exit(0)
