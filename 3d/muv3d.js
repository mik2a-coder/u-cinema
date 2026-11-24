// muv3d.js — branche la mascotte 3D (U Ghjattu-Volpe) sur l'assistant de U CINEMÀ.
// Le même canvas sert au bouton flottant (plein corps) et à l'en-tête du panneau (gros plan).
// Sans WebGL ou si le modèle échoue, les portraits 2D d'origine restent en place.
import { Mascot3D } from './mascot3d.js';

const q = (s) => document.querySelector(s);
const webgl = () => { try { const c = document.createElement('canvas'); return !!(c.getContext('webgl2') || c.getContext('webgl')); } catch (e) { return false; } };
if (webgl()) init().catch((e) => console.warn('[muv3d] 3D indisponible, portraits 2D conservés', e));

async function init() {
  const vp = q('.viewport'), fabHost = q('#muvFabSvg'), avHost = q('#muvAv');
  if (!fabHost) return;
  const reduced = () => !!(vp && vp.classList.contains('rm')) || matchMedia('(prefers-reduced-motion: reduce)').matches;

  const slot = document.createElement('span'); slot.className = 'muv-3d fab'; slot.setAttribute('aria-hidden', 'true');
  slot.style.cssText = 'position:fixed;left:-9999px;top:0;width:104px;height:118px'; document.body.appendChild(slot);
  const m = new Mascot3D(slot); await m.ready;
  const home = () => { slot.style.cssText = ''; slot.className = 'muv-3d fab'; fabHost.replaceChildren(slot); slot.appendChild(m.canvas); m.container = slot; m.setView('full'); m.resize(); };
  const inHeader = () => { if (!avHost) return; const s = document.createElement('span'); s.className = 'muv-3d face'; avHost.replaceChildren(s); s.appendChild(m.canvas); m.container = s; m.setView('head'); m.resize(); };
  home(); q('#muvFab').classList.add('is3d'); window.MV3D = m;

  // ---- une seule animation : assis, en attente (Idle). Posture fixe.
  m.play('Idle');
  const o1 = mvOpen, o2 = mvClose;
  mvOpen = function () { const r = o1.apply(this, arguments); inHeader(); sync(); return r; };
  mvClose = function () { const r = o2.apply(this, arguments); setTimeout(() => { if (!MV.open) { home(); sync(); } }, 320); return r; };
  m.follow = false; // posture fixe : l'animation Idle tourne, mais le corps ne suit pas la souris

  // ---- économie : pause hors accueil / onglet masqué / animations réduites
  const visible = () => m.container.offsetParent !== null && !document.hidden;
  function sync() { if (visible() && !reduced()) m.start(); else { m.stop(); if (visible()) m.renderOnce(); } }
  document.addEventListener('visibilitychange', sync);
  new MutationObserver(sync).observe(vp, { attributes: true, attributeFilter: ['class'] });
  new MutationObserver(sync).observe(q('#muv'), { attributes: true, attributeFilter: ['data-scr'] });
  setInterval(sync, 1500); addEventListener('resize', () => m.resize()); sync();
}
