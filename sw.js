// Service worker file: sw.js

// Install event: log a message when installed
self.addEventListener('install', function (event) {
  console.log('Service Worker installed');
});

// Activate event: log a message when activated
self.addEventListener('activate', (event) => {
  console.log('Service Worker activated');
});

self.addEventListener('fetch', function (event) {
  event.respondWith(
    caches.match(event.request).then(function (response) {
      return response || fetch(event.request);
    })
  );
});
