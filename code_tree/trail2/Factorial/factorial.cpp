#include <iostream>

using namespace std;

int N;

int Factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    
    return n * Factorial(n - 1);
}

int main() {
    cin >> N;

    cout << Factorial(N);

    return 0;
}