#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string> &strs) {
    map<vector<int>, vector<string>> m;

    for (int i = 0; i < strs.size(); i++) {
      vector<int> anagram(26, 0);

      for (int j = 0; j < strs[i].size(); j++) {
        anagram[strs[i][j] - 'a']++;
      }

      m[anagram].push_back(strs[i]);
    }

    vector<vector<string>> res;
    for (auto p : m)
      res.push_back(p.second);

    return res;
  }
};