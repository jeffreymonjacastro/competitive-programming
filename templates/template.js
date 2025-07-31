const MOD = 1e9 + 7;

function binPow(a, b) {
  a %= MOD;
  let result = 1;
  while (b > 0) {
    if (b & 1) result = (result * a) % MOD;
    a = (a * a) % MOD;
    b >>= 1;
  }
  return result;
}

const gcd = (a, b) => b === 0 ? a : gcd(b, a % b);
const lcm = (a, b) => (a * b) / gcd(a, b);

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin
});

let lines = [];
rl.on('line', (line) => {
  lines.push(line);
});

function solve() { }

rl.on('close', () => {
  let t = 1;

  while (t--) {
    solve();
  }
});