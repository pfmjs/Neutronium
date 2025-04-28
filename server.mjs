// server.mjs
import express from 'express';
const app = express();
const PORT = 1000

export function server() {
  app.use(express.static('public'));

  app.listen(PORT, () => {
    console.log(`Server started at http://localhost:${PORT}`);
  });
}
