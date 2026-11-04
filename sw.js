// Văn Phú Đà Lạt – offline support. Bump VERSION when the site changes in a way guests must see right away.
const VERSION = "vp-v2";
const CORE = ["/", "/dalat-motorbike-rental/", "/vi/thue-xe-may-da-lat/", "/id/sewa-motor-dalat/", "/id/restoran-halal-dalat/", "/manifest.json", "/icons/icon-192.png"];

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(VERSION).then((c) => Promise.all(CORE.map((u) => c.add(u).catch(() => null)))).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== VERSION).map((k) => caches.delete(k)))).then(() => self.clients.claim()));
});

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  // Large PDFs are never cached by the browser store; fetch them as usual.
  if (url.pathname.startsWith("/files/")) return;
  // TikTok covers (276 images on the villa page): leave to the normal browser cache, never the offline store.
  if (url.pathname.startsWith("/img/tiktok/")) return;

  if (req.mode === "navigate") {
    // Pages: network first, so guests see fresh prices; fall back to the saved copy when offline.
    e.respondWith(
      fetch(req).then((res) => {
        const copy = res.clone();
        caches.open(VERSION).then((c) => c.put(req, copy)).catch(() => {});
        return res;
      }).catch(() => caches.match(req).then((hit) => hit || caches.match(url.pathname) || caches.match("/")))
    );
    return;
  }

  // Images, fonts and icons: cache first, then save a copy.
  if (url.pathname.startsWith("/img/") || url.pathname.startsWith("/fonts/") || url.pathname.startsWith("/icons/")) {
    e.respondWith(caches.match(req).then((hit) => hit || fetch(req).then((res) => {
      const copy = res.clone();
      caches.open(VERSION).then((c) => c.put(req, copy)).catch(() => {});
      return res;
    })));
  }
});
