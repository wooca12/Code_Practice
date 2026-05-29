#include <iostream>
using namespace std;

int Func(int n) {
    if (n == 1)
        return 1;
    if (n == 2)
        return 2;

    return n + Func(n - 2);

}

int main() {
    int n;
    cin >> n;

    cout << Func(n);

    return 0;
}