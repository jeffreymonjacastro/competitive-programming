// Normal Problem
// Tags: implementation, strings
// Level: 800
#include <iostream>

using namespace std;

#define cpu()                                                                  \
  ios::sync_with_stdio(false);                                                 \
  cin.tie(nullptr)
typedef long long ll;
typedef long double lld;

void solve() {
  string a, res = "";
  cin >> a;

  for (int i = a.size() - 1; i >= 0; i--) {
    if (a[i] == 'p')
      res += 'q';
    else if (a[i] == 'q')
      res += 'p';
    else
      res += 'w';
  }
  cout << res << endl;
}

int main() {
  cpu();
  int t = 1;
  cin >> t;

  while (t--)
    solve();
}
