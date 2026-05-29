#include <iostream>

using namespace std;

int a, b, c;


int Sum(int n) {
    if (n < 10)
        return n;
    return Sum(n / 10) + n % 10;
}

int main() {
    cin >> a >> b >> c;

    cout << Sum(a * b * c);

    return 0;
}