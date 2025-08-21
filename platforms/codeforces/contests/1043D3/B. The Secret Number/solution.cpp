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
#define print(x) cout << x << " "

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
  ll n;
  cin >> n;
  string s = to_string(n);

  auto oneDigit = [&]() {
    set<char> digits(s.begin(), s.end());
    return digits.size() == 1;
  };

  auto divisores = [](ll num) {
    vector<ll> div;
    for (ll i = 1; i * i <= num; i++) {
      if (num % i == 0) {
        div.push_back(i);
        if (i != num / i) {
          div.push_back(num / i);
        }
      }
    }
    sort(div.begin(), div.end(), greater<ll>());
    return div;
  };

  auto rep = [](const string &str, int cnt) {
    string ret;
    for (int i = 0; i < cnt; i++) {
      ret += str;
    }
    return ret;
  };

  if (!oneDigit()) {
    println(0);
    return;
  }

  int l = s.length();

  if (l % 2 == 1) {
    println(0);
    return;
  }

  vector<ll> div = divisores(l / 2);

  println(div.size());

  vector<string> res;

  for (ll d : div) {
    ll len = l - d;

    string result;

    if (d == (l / 2)) {
      for (ll i = 0; i < len; i++) {
        result += s[0];
      }
    } else if (d == 1) {
      for (ll i = 0; i < len; i++) {
        if (i % 2 == 0) {
          result += s[0];
        } else {
          result += '0';
        }
      }
    } else {
      string pattern = "";
      for (ll i = 0; i < d; i++) {
        pattern += s[0];
      }
      for (ll i = 0; i < d; i++) {
        pattern += '0';
      }

      ll full = len / (2 * d);
      result = rep(pattern, full);

      ll remaining = len - result.length();
      for (ll i = 0; i < remaining; i++) {
        if (i < d) {
          result += s[0];
        } else {
          result += '0';
        }
      }
    }

    res.push_back(result);
  }

  for (string &r : res) {
    print(r);
  }

  cout << "\n";
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
