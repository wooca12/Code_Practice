#include <iostream>
using namespace std;

int main() {
    int a1, a2, b1, b2;

    cin >> a1 >> a2 >> b1 >> b2;

    if ((a1 > b1) || (a1 == b1) && a2 > b2)
        cout << "A" << endl;
    else 
        cout << "B" << endl;
    return 0;
}