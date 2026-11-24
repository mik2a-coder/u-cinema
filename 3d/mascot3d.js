// mascot3d.js — U Ghjattu-Volpe (modèle rigué final, 16 clips) dans un petit canvas three.js transparent.
import * as THREE from 'three';
import { GLTFLoader } from './vendor/GLTFLoader.js';

const LOOPS = new Set(['Idle', 'Marche', 'Course', 'Course_rapide', 'Furtif_cacher', 'Grimper', 'Allonge_detente', 'Regarde_papillon']);
const clamp = (x, a, b) => Math.max(a, Math.min(b, x));

export class Mascot3D {
  constructor(container, { url = './3d/models/ghjattu.glb' } = {}) {
    this.container = container; this.pointer = { x: 0, y: 0 }; this.look = { x: 0, y: 0 }; this.follow = true;
    this.running = false; this.clips = {}; this.cur = null; this.view = 'full';
    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'low-power' });
    this.renderer.setPixelRatio(Math.min(devicePixelRatio || 1, 2)); this.renderer.setClearColor(0x000000, 0);
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    this.canvas = this.renderer.domElement; container.appendChild(this.canvas);
    this.scene = new THREE.Scene();
    this.scene.add(new THREE.HemisphereLight(0xffffff, 0x4a3a30, 1.5));
    const k = new THREE.DirectionalLight(0xfff0e0, 3); k.position.set(2, 3, 3); this.scene.add(k);
    this.camera = new THREE.PerspectiveCamera(28, 1, 0.05, 50);
    this.holder = new THREE.Group(); this.scene.add(this.holder);
    this.clock = new THREE.Clock();
    this.ready = new GLTFLoader().loadAsync(url).then((g) => {
      this.model = g.scene; this.holder.add(this.model);
      this.model.traverse((o) => { if (o.isMesh) o.frustumCulled = false; });
      this.mixer = new THREE.AnimationMixer(this.model);
      g.animations.forEach((c) => { this.clips[c.name] = this.mixer.clipAction(c); });
      this.mixer.addEventListener('finished', () => { this.cur = null; this.onDone && this.onDone(); });
      this.setView('full'); this.play('Idle'); return this;
    });
  }
  // cadrages : plein corps (bouton) ou gros plan tête (en-tête du panneau)
  setView(v) {
    this.view = v;
    const V = { full: { pos: [1.9, 0.55, 5.4], t: [0, -0.05, 0], fov: 26 }, head: { pos: [1.0, 0.95, 2.6], t: [-0.1, 0.55, 0], fov: 26 } }[v];
    this.camera.position.set(...V.pos); this.camera.fov = V.fov; this.camera.lookAt(...V.t); this.camera.updateProjectionMatrix();
  }
  resize() {
    const w = this.container.clientWidth, h = this.container.clientHeight; if (!w || !h) return;
    this.renderer.setSize(w, h, false); this.canvas.style.width = '100%'; this.canvas.style.height = '100%';
    this.camera.aspect = w / h; this.camera.updateProjectionMatrix();
  }
  attach(el, view) { el.replaceChildren(this.canvas); this.container = el; this.setView(view); this.resize(); }
  play(name, fade = 0.3) {
    const a = this.clips[name]; if (!a || a === this.cur) return;
    a.reset(); a.setLoop(LOOPS.has(name) ? THREE.LoopRepeat : THREE.LoopOnce, Infinity); a.clampWhenFinished = true;
    if (this.cur) a.crossFadeFrom(this.cur, fade, false); a.play(); this.cur = a; this.name = name;
  }
  setPointer(px, py) {
    const r = this.container.getBoundingClientRect();
    this.pointer.x = clamp((px - (r.left + r.width / 2)) / 320, -1, 1); this.pointer.y = clamp(-(py - (r.top + r.height * 0.4)) / 320, -1, 1);
  }
  start() { if (!this.running) { this.running = true; this.clock.getDelta(); this.renderer.setAnimationLoop(() => this.frame()); } }
  stop() { this.running = false; this.renderer.setAnimationLoop(null); }
  frame() { this.step(Math.min(this.clock.getDelta(), 0.05)); this.renderer.render(this.scene, this.camera); }
  renderOnce() { if (this.model) { this.mixer.update(0); this.step(0); this.renderer.render(this.scene, this.camera); } }
  // gros plan : la caméra suit l'os de la tête, le visage reste centré quelle que soit la pose
  _headCam() {
    const h = this.model && this.model.getObjectByName('Head'); if (!h) return;
    this.model.updateMatrixWorld(true); const p = h.getWorldPosition(new THREE.Vector3());
    this.camera.position.set(p.x + 1.0, p.y + 0.4, p.z + 3.3); this.camera.lookAt(p.x, p.y + 0.12, p.z);
  }
  step(dt) {
    if (this.mixer) this.mixer.update(dt);
    if (this.view === 'head') this._headCam();
    // le corps se tourne doucement vers le pointeur
    const k = 1 - Math.exp(-dt * 4), wx = this.follow ? this.pointer.x : 0;
    this.look.x += (wx - this.look.x) * k; this.look.y += ((this.follow ? this.pointer.y : 0) - this.look.y) * k;
    this.holder.rotation.y = this.look.x * 0.45; this.holder.rotation.x = -this.look.y * 0.06;
  }
}
