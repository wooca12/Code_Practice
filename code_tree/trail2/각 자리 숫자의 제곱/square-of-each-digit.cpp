#include <iostream>
using namespace std;

int F(int n) {
    if (n == 0)
        return 0;
    return F(n / 10) + (n % 10) * (n % 10);
}

int main() {
    int n;
    cin >> n;

    cout << F(n) << endl;

    return 0;
}