#include <iostream>
using namespace std;

int Func(int n) {
    if (n == 1)
        return 0;
    if (n % 2 == 0)
        return 1 + Func(n / 2);
    else    
        return 1 + Func(n / 3);
}

int main() {
    int n;
    cin >> n;

    cout << Func(n);
    return 0;
}