#include <iostream>
using namespace std;

int main() {
    int a = 2, b = 5;
    int tmp;
    tmp = a;
    a = b;
    b = tmp;

    cout << a << endl;
    cout << b << endl;
    return 0;
}