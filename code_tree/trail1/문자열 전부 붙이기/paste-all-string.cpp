#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    string a = "";
    
    for (int i = 0; i < n; i++) {
        string b;
        cin >> b;
        a.append(b);
    }
    cout << a << endl;
    return 0;
}