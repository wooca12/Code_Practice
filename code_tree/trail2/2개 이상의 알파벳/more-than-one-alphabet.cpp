#include <iostream>
#include <string>

using namespace std;


// ****** < MY CODE > *****
// bool IsMoreTwoAlp(string a) {
//     string alphabets = "";
//     int cnt = 0;

//     for (int i = 0; i < a.length(); i++) {
//         if (alphabets.find(a[i]) == string::npos) {
//             cnt++;
//             alphabets += a[i];
//         }
//     }
//     return (cnt >= 2);
// }

bool IsMoreTwoAlp(string a) {
    int len = a.length();

    for (int i = 0; i < len; i++) {
        if (a[i] != a[0]) {
            return true;
        }
    }
    return false;
}

int main() {
    string A;
    cin >> A;

    if (IsMoreTwoAlp(A)) {
        cout << "Yes";
    }
    else {
        cout << "No";
    }
    return 0;
}