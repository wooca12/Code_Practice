#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;

    string n1 = "", n2 = "";
    for (int i = 0; i < a.length(); i++) {
        if (isdigit(a[i]) != 0)
            n1 += a[i];
        else
            break;
    }
    for (int i = 0; i < b.length(); i++) {
        if (isdigit(b[i]) != 0)
            n2 += b[i];
        else 
            break;
            
    }
    cout << stoi(n1) + stoi(n2) << endl;

    return 0;
}