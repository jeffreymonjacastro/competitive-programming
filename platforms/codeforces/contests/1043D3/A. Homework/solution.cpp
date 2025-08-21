#include <bits/stdc++.h>

using namespace std;
#define cpu()                  \
  ios::sync_with_stdio(false); \
  cin.tie(nullptr);
#define ll long long
#define lld long double
#define pii pair<int, int>
#define pdd pair<double, double>
#define f first
#define s second
#define println(x) cout << x << "\n"
#define print(x) cout << x

const int mod = 1e9 + 7;

ll binPow(ll a, ll b) {
  a %= mod;
  ll result = 1;
  while (b > 0) {
    if (b & 1LL)
      result = (result * a) % mod;
    a = (a * a) % mod;
    b >>= 1;
  }
  return result;
}

void solve() {
  int n, m;
  string a, b, c;
  cin >> n >> a >> m >> b >> c;

  for (int i = 0; i < m; i++) {
    if (c[i] == 'D')
      a = a + b[i];
    else
      a = b[i] + a;
  }

  println(a);
}

signed main() {
  cpu();
  int t;
  t = 1;
  cin >> t;
  while (t--)
    solve();
  return 0;
}
