/* U CINEMÀ – service worker : l'appli reste utilisable hors ligne */
const CACHE = 'cinelux2-v26';
const ASSETS = ['./', './index.html', './manifest.webmanifest', './fonts/fonts.css',
  './fonts/BebasNeue-400.woff2', './fonts/Inter-400.woff2',
  './fonts/AtkinsonHyperlegible-400.woff2', './fonts/AtkinsonHyperlegible-700.woff2',
  './icons/icon-192.png', './icons/icon-512.png', './icons/apple-touch-icon.png',
  './img/hotb.jpg', './img/lesmis.jpg', './img/odyssey.jpg', './img/spiderman.jpg', './img/toystory5.jpg', './img/hailmary.jpg', './img/michael.png', './img/supergirl.jpg', './img/prada2.png', './img/mariogalaxy.jpg', './img/mandalorian.jpg', './img/moana.jpg', './img/hungergames.jpg', './img/focker.jpg', './img/avengers.jpg', './img/dune3.jpg', './img/angrybirds3.jpg', './img/jumanji.jpg', './img/scene/hotb.jpg', './img/scene/lesmis.jpg', './img/scene/odyssey.jpg', './img/scene/spiderman.jpg', './img/scene/toystory5.jpg', './img/scene/hailmary.jpg', './img/scene/michael.jpg', './img/scene/supergirl.jpg', './img/scene/prada2.jpg', './img/scene/mariogalaxy.jpg', './img/scene/mandalorian.jpg', './img/scene/moana.jpg', './img/scene/hungergames.jpg', './img/scene/focker.jpg', './img/scene/avengers.jpg', './img/scene/dune3.jpg', './img/scene/angrybirds3.jpg', './img/scene/jumanji.jpg', './img/people/david-ayer.jpg', './img/people/brad-pitt.jpg', './img/people/j-k-simmons.jpg', './img/people/anna-lambe.jpg', './img/people/fred-cavaye.jpg', './img/people/vincent-lindon.jpg', './img/people/tahar-rahim.jpg', './img/people/noemie-merlant.jpg', './img/people/christopher-nolan.jpg', './img/people/matt-damon.jpg', './img/people/tom-holland.jpg', './img/people/anne-hathaway.jpg', './img/people/robert-pattinson.jpg', './img/people/lupita-nyong-o.jpg', './img/people/samantha-morton.jpg', './img/people/destin-daniel-cretton.jpg', './img/people/zendaya.jpg', './img/people/sadie-sink.jpg', './img/people/jacob-batalon.jpg', './img/people/jon-bernthal.jpg', './img/people/florence-pugh.jpg', './img/people/andrew-stanton.jpg', './img/people/joan-cusack.jpg', './img/people/tom-hanks.jpg', './img/people/tim-allen.jpg', './img/people/conan-o-brien.jpg', './img/people/greta-lee.jpg', './img/people/ryan-gosling.jpg', './img/people/sandra-huller.jpg', './img/people/james-ortiz.jpg', './img/people/lionel-boyce.jpg', './img/people/antoine-fuqua.jpg', './img/people/jaafar-jackson.jpg', './img/people/nia-long.jpg', './img/people/laura-harrier.jpg', './img/people/jessica-sula.jpg', './img/people/craig-gillespie.jpg', './img/people/milly-alcock.jpg', './img/people/matthias-schoenaerts.jpg', './img/people/eve-ridley.jpg', './img/people/david-krumholtz.jpg', './img/people/emily-beecham.jpg', './img/people/david-corenswet.jpg', './img/people/david-frankel.jpg', './img/people/meryl-streep.jpg', './img/people/emily-blunt.jpg', './img/people/justin-theroux.jpg', './img/people/kenneth-branagh.jpg', './img/people/stanley-tucci.jpg', './img/people/aaron-horvath.jpg', './img/people/michael-jelenic.jpg', './img/people/chris-pratt.jpg', './img/people/anya-taylor-joy.jpg', './img/people/charlie-day.jpg', './img/people/jack-black.jpg', './img/people/keegan-michael-key.jpg', './img/people/benny-safdie.jpg', './img/people/jon-favreau.jpg', './img/people/pedro-pascal.jpg', './img/people/jeremy-allen-white.jpg', './img/people/brendan-wayne.jpg', './img/people/lateef-crowder.jpg', './img/people/jonny-coyne.jpg', './img/people/martin-scorsese.jpg', './img/people/thomas-kail.jpg', './img/people/dwayne-johnson.jpg', './img/people/rena-owen.jpg', './img/people/john-tui.jpg', './img/people/frankie-adams.jpg', './img/people/jemaine-clement.jpg', './img/people/catherine-laga-aia.jpg', './img/people/francis-lawrence.jpg', './img/people/jesse-plemons.jpg', './img/people/ralph-fiennes.jpg', './img/people/glenn-close.jpg', './img/people/ben-wang.jpg', './img/people/kieran-culkin.jpg', './img/people/john-hamburg.jpg', './img/people/robert-de-niro.jpg', './img/people/ben-stiller.jpg', './img/people/ariana-grande.jpg', './img/people/owen-wilson.jpg', './img/people/blythe-danner.jpg', './img/people/teri-polo.jpg', './img/people/robert-downey-jr.jpg', './img/people/chris-hemsworth.jpg', './img/people/paul-rudd.jpg', './img/people/anthony-mackie.jpg', './img/people/denis-villeneuve.jpg', './img/people/timothee-chalamet.jpg', './img/people/jason-momoa.jpg', './img/people/rebecca-ferguson.jpg', './img/people/isaach-de-bankole.jpg', './img/people/jason-sudeikis.jpg', './img/people/josh-gad.jpg', './img/people/emma-myers.jpg', './img/people/rachel-bloom.jpg', './img/people/walker-scobell.jpg', './img/people/danny-mcbride.jpg', './img/people/jake-kasdan.jpg', './img/people/kevin-hart.jpg', './img/people/karen-gillan.jpg', './img/people/nick-jonas.jpg', './img/people/awkwafina.jpg', './img/mascot-head.png', './img/mascot.png', './img/food/combo2.jpg', './img/food/combo.jpg', './img/food/solo.jpg', './img/food/cola2.jpg', './img/food/chocolat2.jpg', './img/food/nachos2.jpg', './img/food/popcorn3.jpg', './img/food/candy.jpg', './img/food/chips.jpg', './img/food/chocolate.jpg', './img/food/cola.jpg', './img/food/cookie.jpg', './img/food/hotdog.jpg', './img/food/icecream.jpg', './img/food/milkshake.jpg', './img/food/nachos.jpg', './img/food/popcorn.jpg', './img/food/popcorn2.jpg', './img/food/pretzel.jpg', './img/food/soda.jpg'];

/* À l'installation on contourne le cache HTTP : on veut toujours la dernière version des fichiers */
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE)
    .then(c => c.addAll(ASSETS.map(u => new Request(u, { cache: 'reload' }))))
    .then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(k => Promise.all(k.filter(x => x !== CACHE).map(x => caches.delete(x))))
    .then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  const r = e.request;
  if (r.method !== 'GET' || new URL(r.url).origin !== location.origin) return;
  /* la page : réseau d'abord (mises à jour immédiates), cache en secours hors ligne */
  if (r.mode === 'navigate') {
    e.respondWith(fetch(r).then(res => { const c = res.clone(); caches.open(CACHE).then(x => x.put('./index.html', c)); return res; })
      .catch(() => caches.match('./index.html')));
    return;
  }
  /* le reste : cache tout de suite, mise à jour en arrière-plan */
  e.respondWith(caches.match(r).then(m => {
    const net = fetch(r, { cache: 'no-cache' }).then(res => { if (res.ok) { const c = res.clone(); caches.open(CACHE).then(x => x.put(r, c)); } return res; }).catch(() => m);
    return m || net;
  }));
});
