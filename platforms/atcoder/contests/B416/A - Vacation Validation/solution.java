import java.io.*;
import java.util.*;

class Solution {
  static final int MOD = 1000000007;
  static final long INF = Long.MAX_VALUE;

  static FastReader in = new FastReader();
  static PrintWriter out = new PrintWriter(System.out);

  static long binPow(long a, long b) {
    a %= MOD;
    long result = 1;
    while (b > 0) {
      if ((b & 1) == 1)
        result = (result * a) % MOD;
      a = (a * a) % MOD;
      b >>= 1;
    }
    return result;
  }

  static long gcd(long a, long b) {
    while (b != 0) {
      long temp = b;
      b = a % b;
      a = temp;
    }
    return a;
  }

  static long lcm(long a, long b) {
    return (a * b) / gcd(a, b);
  }

  static void solve() {
    String[] firstLine = in.nextLine().split(" ");
    int L = Integer.parseInt(firstLine[1]);
    int R = Integer.parseInt(firstLine[2]);

    String S = in.nextLine();

    for (int i = L - 1; i < R; i++) {
      if (S.charAt(i) != 'o') {
        out.println("No");
        return;
      }
    }
    out.println("Yes");
  }

  public static void main(String[] args) {
    int t = 1;
    // t = in.nextInt();
    while (t-- > 0) {
      solve();
    }
    out.close();
  }

  static class FastReader {
    BufferedReader br;
    StringTokenizer st;

    public FastReader() {
      br = new BufferedReader(new InputStreamReader(System.in));
    }

    String next() {
      while (st == null || !st.hasMoreElements()) {
        try {
          st = new StringTokenizer(br.readLine());
        } catch (IOException e) {
          e.printStackTrace();
        }
      }
      return st.nextToken();
    }

    int nextInt() {
      return Integer.parseInt(next());
    }

    long nextLong() {
      return Long.parseLong(next());
    }

    double nextDouble() {
      return Double.parseDouble(next());
    }

    String nextLine() {
      String str = "";
      try {
        str = br.readLine();
      } catch (IOException e) {
        e.printStackTrace();
      }
      return str;
    }
  }
}
