const http = require('http');
const fs = require('fs');

const server = http.createServer((req, res) => {
  fs.readFile('attack.html', (err, data) => {
    if (err) {
      res.writeHead(500);
      res.end('Error reading file');
      return;
    }

    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write(data);
    res.end();
  });
});

server.listen(8080, () => {
  console.log('Server running on http://localhost:8080');
});
