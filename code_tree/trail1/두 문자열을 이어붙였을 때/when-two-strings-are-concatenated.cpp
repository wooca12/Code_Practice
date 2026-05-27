#include <iostream>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;
    if (a + b == b + a)
        cout << "true" << endl;
    else
        cout << "false" << endl;
    return 0;
}