#include <iostream>
using namespace std;

int IsPrime(int n) {
    for (int i = 2; i < n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}
int main() {
    int a, b;
    cin >> a >> b;

    int sum = 0;

    for (int i = a; i <= b; i++) {

        if (IsPrime(i)) {
            sum += i;
        }
    }

    cout << sum << endl;

    return 0;
}