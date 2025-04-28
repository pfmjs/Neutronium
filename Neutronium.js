// index.js
const server = require('./server.mjs')
const webviewModule = require('webview'); // Assuming the webview module is in the same folder
const options = {
  url: 'http://localhost', // URL you want to open
  width: 800,  // Width of the window
  height: 600, // Height of the window
};

try {
  // Spawning the process to open a webview with specified options
  const process = webviewModule.spawn(options);
  server.server

  process.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
  });

  process.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  process.on('exit', (code) => {
    console.log(`Process exited with code ${code}`);
  });
} catch (error) {
  console.error('Error starting process:', error);
}
