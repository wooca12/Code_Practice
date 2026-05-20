#include <iostream>
using namespace std;

int main() {
    char x[10];

    for (int i = 0; i < 10; i++) {
        cin >> x[i];
    }
    cout << x[1] << " " << x[4] << " " << x[7] << endl;
    return 0;
}