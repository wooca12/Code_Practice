#include <iostream>
using namespace std;

int main() {
    int a1, a2, b1, b2;

    cin >> a1 >> a2 >> b1 >> b2;

    if (a1 > b1)    
        cout << "A" << endl;
    else if (a1 < b1)
        cout << "B" << endl;
    else {
        if (a2 > b2)
            cout << "A" << endl;
        else if (a2 < b2)
            cout << "B" << endl;
    }
    return 0;
}