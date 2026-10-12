#include <iostream>
using namespace std;

int main() {
    int a;
    cin >> a;
    
    if (a < 0) 
        cout << "ice" << endl;
    else if (a >= 100)
        cout << "vapor" << endl;
    else
        cout << "water" << endl;
    return 0;
}