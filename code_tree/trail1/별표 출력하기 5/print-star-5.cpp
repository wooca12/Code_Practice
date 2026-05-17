#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i; j++) {
            for (int l = 0; l < n - i; l++) {
                cout << "*";
            }
            cout << " ";
        }
        cout << endl;
    }
    return 0;
}