var input = require('fs').readFileSync('./dev/stdin/file.txt', 'utf8');
var lines = input.split('\n');
    
var raio = parseFloat(lines.shift());
console.log("A=" + (3.14159 * Math.pow(raio,2)).toFixed(4));