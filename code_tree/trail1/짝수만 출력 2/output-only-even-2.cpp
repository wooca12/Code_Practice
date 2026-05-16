#include <iostream>
using namespace std;

int main() {
    int a, b, i;
    cin >> b >> a;
    i = b;
    while (i >= a) {
        cout << i << " ";
        i -= 2;
    }
    return 0;
}