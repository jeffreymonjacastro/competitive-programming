#include <bits/stdc++.h>

using namespace std;
#define cpu()                  \
  ios::sync_with_stdio(false); \
  cin.tie(nullptr);
#define ll long long
#define lld long double
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
  int n;
  cin >> n;

  vector<int> a(n - 1);

  for (int i = 0; i < n - 1; i++) {
    cin >> a[i];
  }

  sort(a.begin(), a.end());

  if (a[0] != 1) {
    print(1);
    return;
  }

  for (int i = 1; i < n - 1; i++) {
    if (a[i] - a[i - 1] > 1) {
      print(a[i - 1] + 1);
      return;
    }
  }

  print(a[n - 2] + 1);
}

signed main() {
  cpu();
  int t;
  t = 1;
  // cin >> t;
  while (t--)
    solve();
  return 0;
}
