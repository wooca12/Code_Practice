#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    string total = "";

    for (int i = 0; i < n; i++) {
        string str;
        cin >> str;
        total += str;
    }
    for (int i = 0; i < total.length(); i++) {
        if (i != 0 && (i % 5) == 0)
            cout << endl;
        cout << total[i];
    }
    
    return 0;
}