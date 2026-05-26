#include <iostream>
#include <string>

using namespace std;

string A;

int main() {
    cin >> A;
    string new_A = "";

    char c[1000] = {};
    int n[1000] = {};

    int idx = -1;
    for (int i = 0; i < A.length(); i++) {
        if (c[idx] != A[i]) {
            idx++;
            c[idx] = A[i];
            n[idx]++;
        }
        else {
            n[idx]++;
        }
    }
    for (int i = 0; i <= idx; i++) {
        new_A += c[i] + to_string(n[i]);
    }
    cout << new_A.length() << endl;
    cout << new_A << endl;
    return 0;
}
