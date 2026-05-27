#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    int q;
    cin >> s >> q;

    int len = s.length();

    for (int i = 0; i < q; i++) {
        int n;
        cin >> n;

        if (n == 1) {
            s = s.substr(1, len - 1) + s.substr(0, 1);
        }
        else if (n == 2) {
            s = s.substr(len - 1, 1) + s.substr(0, len - 1);
        }
        else {
            string s1 = "";
            for (int j = len - 1; j >= 0; j--) {
                s1 += s[j];
            }
            s = s1;
        }
        cout << s << endl;
    }

    return 0;
}