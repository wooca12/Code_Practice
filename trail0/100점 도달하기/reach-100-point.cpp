#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int i;
    for (i = n; i <= 100; i++) {
        if (n >= 90)
            cout << "A ";
        else if (n >= 80)
            cout << "B ";
        else if (n >= 70)
            cout << "C ";
        else if (n >= 60)
            cout << "D ";
        else
            cout << "F ";
        n += 1;
    }
    return 0;
}