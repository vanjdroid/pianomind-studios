// PianoMind Studios service worker: lets the app open without internet.
// Change VERSION to force every device to refresh its saved copy.
const VERSION = 'pms-v7';
const CORE = [
  './', './index.html', './piano_mind.html', './manifest.webmanifest',
  './icon-clef-192.png', './icon-clef-512.png', './apple-touch-icon.png',
  './background.png', './background_phone.png', './pebbles_happy.png', './pebbles_asking.png', './pebbles_thinking.png',
  './piano/A1.mp3', './piano/C2.mp3', './piano/Ds2.mp3', './piano/Fs2.mp3', './piano/A2.mp3', './piano/C3.mp3', './piano/Ds3.mp3', './piano/Fs3.mp3', './piano/A3.mp3', './piano/C4.mp3', './piano/Ds4.mp3', './piano/Fs4.mp3', './piano/A4.mp3', './piano/C5.mp3', './piano/Ds5.mp3', './piano/Fs5.mp3', './piano/A5.mp3', './piano/C6.mp3', './piano/Ds6.mp3', './piano/Fs6.mp3', './piano/A6.mp3', './piano/C7.mp3'
];
// Outside sites we may save (Firebase code + fonts). Never Firestore/login traffic.
const CDN = ['www.gstatic.com', 'fonts.googleapis.com', 'fonts.gstatic.com'];

// Firebase code the app needs to start. Saved on the FIRST visit so the app opens offline.
const FIREBASE = ['app', 'auth', 'firestore'].map(n => `https://www.gstatic.com/firebasejs/10.12.0/firebase-${n}-compat.js`);

self.addEventListener('install', e => {
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(CORE).then(() =>
    // If Firebase can't be saved right now, still install; it gets saved on a later visit.
    Promise.all(FIREBASE.map(u => c.add(new Request(u, { mode: 'cors' })).catch(() => {})))
  )).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== VERSION).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  const sameSite = url.origin === self.location.origin;
  if (!sameSite && !CDN.includes(url.hostname)) return; // leave Firebase data alone

  // Pages: try the internet first so updates show up; use saved copy when offline.
  if (req.mode === 'navigate') {
    e.respondWith(
      // no-cache = always ask GitHub for the newest version (skips its 10-minute cache)
      fetch(req.url, { cache: 'no-cache' }).then(res => {
        const copy = res.clone();
        caches.open(VERSION).then(c => c.put(req, copy));
        return res;
      }).catch(() => caches.match(req, { ignoreSearch: true })
        .then(r => r || caches.match('./piano_mind.html')))
    );
    return;
  }

  // Everything else: use saved copy right away, refresh it in the background.
  e.respondWith(
    caches.match(req, { ignoreSearch: sameSite }).then(cached => {
      const net = fetch(req).then(res => {
        if (res.ok || res.type === 'opaque') {
          const copy = res.clone();
          caches.open(VERSION).then(c => c.put(req, copy));
        }
        return res;
      }).catch(() => cached);
      return cached || net;
    })
  );
});
