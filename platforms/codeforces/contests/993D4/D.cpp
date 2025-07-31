// Harder Problem
// Tags: Constructive algorithms, greedy, math
// Level: 1100
#include <iostream>
#include <set>
#include <vector>

using namespace std;

#define cpu()                                                                  \
  ios::sync_with_stdio(false);                                                 \
  cin.tie(nullptr);
typedef long long ll;
typedef long double lld;

void solve() {
  int n;

  cin >> n;

  vector<int> a(n);
  vector<int> b;
  set<int> s;

  for (int i = 0; i < n; i++) {
    cin >> a[i];
    s.insert(i + 1);
  }

  for (int i : a) {
    if (s.find(i) != s.end()) {
      b.push_back(i);
      s.erase(i);
    } else {
      b.push_back(*s.begin());
      s.erase(s.begin());
    }
  }

  for (int num : b) {
    cout << num << " ";
  }
  cout << endl;
}

int main() {
  cpu();
  int t = 1;
  cin >> t;

  while (t--)
    solve();
}
