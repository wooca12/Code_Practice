#include <iostream>
using namespace std;

int main() {
    int s, age;
    cin >> s;
    cin >> age;

    if (s == 0) {
        if (age >= 19) 
            cout << "MAN" << endl;
        else
            cout << "BOY" << endl;
    }
    else {
        if (age >= 19) 
            cout << "WOMAN" << endl;
        else
            cout << "GIRL" << endl;
    }

    
    return 0;
}