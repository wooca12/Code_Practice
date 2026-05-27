#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    int n;

    cin >> s >> n;

    for (int i = 0; i < n; i++) {
        int q;
        cin >> q;
        if (q == 1) {
            int a, b;
            cin >> a >> b;

            char tmp;
            tmp = s[a - 1];
            s[a - 1] = s[b - 1];
            s[b - 1] = tmp;
        }
        else {
            char x, y;
            cin >> x >> y;

            for (int j = 0; j < s.length(); j++) {
                if (s[j] == x)
                    s[j] = y;
            }
        }
        cout << s << endl;
    }

    return 0;
}