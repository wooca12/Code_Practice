#include <iostream>

using namespace std;

int n;

int Recursion(int n) {
    if (n == 1)
        return 0;
    if (n % 2 == 0)
        n /= 2;
    else
        n = n * 3 + 1;
    return 1 + Recursion(n);
}

int main() {
    cin >> n;

    cout << Recursion(n);

    return 0;
}