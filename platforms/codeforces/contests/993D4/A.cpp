// Easy Problem
// Tags: Brute Force, math
// Level: 800
#include <iostream>

using namespace std;

#define cpu()                                                                  \
  ios::sync_with_stdio(false);                                                 \
  cin.tie(nullptr)
typedef long long ll;
typedef long double lld;

void solve() {
  int n, count = 0;
  cin >> n;

  for (int a = 1; a < n; a++) {
    for (int b = 1; b < n; b++) {
      if (a + b == n) {
        count++;
      }
    }
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
