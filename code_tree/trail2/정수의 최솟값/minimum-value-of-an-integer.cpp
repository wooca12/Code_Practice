#include <iostream>
using namespace std;

int Min(int a, int b, int c) {
    return min(min(a, b), c);
}

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    int min = Min(a, b, c);
    cout << min << endl;

    return 0;
}