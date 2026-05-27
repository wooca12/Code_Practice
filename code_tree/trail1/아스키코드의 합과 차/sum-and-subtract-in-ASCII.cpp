#include <iostream>
using namespace std;

int main() {
    char a, b;
    cin >> a >> b;

    int a_n = int(a), b_n = int(b);
    int diff = a_n > b_n ? a_n - b_n : b_n - a_n;

    cout << a_n + b_n << " " << diff;

    return 0;
}