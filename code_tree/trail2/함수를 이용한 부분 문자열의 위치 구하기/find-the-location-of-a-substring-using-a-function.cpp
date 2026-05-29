#include <iostream>
#include <string>
using namespace std;


// ***** < MY CODE> *****
// int FindIndex(string a, string b) {
//     int idx = -1;

//     int n1 = a.length();
//     int n2 = b.length();

//     for (int i = 0; i < n1; i++) {
//         if (a.substr(i, n2) == b) {
//             idx = i;
//             break;
//         }
//     }

//     return idx;
// }

bool IsSub(int start_idx, string a, string b) {
    int len = (int) b.size();
    
    for (int i = 0; i < len; i++) {
        if (a[start_idx + i] != b[i])
            return false;
    }
    return true;
}

int FindIndex(string a, string b) {
    int len = (int) a.size();
    for (int i = 0; i < len; i++) {
        if (IsSub(i, a, b)) 
            return i;
    }
    return -1;
}

int main() {
    string a, b;
    cin >> a >> b;

    int ans = FindIndex(a, b);
    cout << ans << endl;
    return 0;
}