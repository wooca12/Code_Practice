#include <iostream>
#include <algorithm>
#include <string>
#define MAX_N 100

using namespace std;

int main() {
    int n, k;
    string t;

    cin >> n >> k >> t;

    string str[MAX_N];

    for (int i = 0; i < n; i++) {
        cin >> str[i];
    }

    string t_str[MAX_N];
    int idx = 0;
    for (int i = 0; i < n; i++) {
        if (str[i].substr(0, t.size()) == t) {
            t_str[idx] = str[i];
            idx++;
        }
    }    
    sort(t_str, t_str + idx);

    cout << t_str[k - 1] << endl;

    return 0;
}