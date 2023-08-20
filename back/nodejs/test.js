const fs = require('fs');
const path = require('path')
let img = fs.readFileSync(path.join(__dirname,"uploads/test1asdf.png"));
img =Uint8Array.from(img).buffer;
console.log(img);