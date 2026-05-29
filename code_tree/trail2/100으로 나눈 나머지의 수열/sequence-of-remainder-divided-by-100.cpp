#include <iostream>
using namespace std;

int Recursion(int n) {
    if (n == 1)
        return 2;
    if (n == 2)
        return 4;
    return (Recursion(n - 1) * Recursion(n - 2)) % 100;
}

int main() {
    int n;
    cin >> n;

    cout << Recursion(n);

    return 0;
}