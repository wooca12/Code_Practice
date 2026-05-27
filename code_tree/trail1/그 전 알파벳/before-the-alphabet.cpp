#include <iostream>
using namespace std;

int main() {
    char c;
    cin >> c;

    if (c == 'a') 
        cout << char(c + 25) << endl;
    else
        cout << char(c - 1) << endl;

    return 0;
}