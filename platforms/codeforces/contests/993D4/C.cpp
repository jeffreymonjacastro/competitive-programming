// Hard Problem
// Tags: greedy, math
// Level: 800
#include <iostream>

using namespace std;

#define cpu()                                                                  \
  ios::sync_with_stdio(false);                                                 \
  cin.tie(nullptr)
typedef long long ll;
typedef long double lld;

void solve() {
  int m, n, a, b, c, count = 0;
  cin >> m >> a >> b >> c;
  n = m;
  if (a <= m) {
    count += a;
    m -= a;
  } else {
    count += m;
    m = 0;
  }

  if (b <= n) {
    count += b;
    n -= b;
  } else {
    count += n;
    n = 0;
  }

  if (c <= m + n) {
    count += c;
  } else {
    count += (m + n);
  }

  cout << count << endl;
}

int main() {
  cpu();
  int t = 1;
  cin >> t;

  while (t--)
    solve();
}
