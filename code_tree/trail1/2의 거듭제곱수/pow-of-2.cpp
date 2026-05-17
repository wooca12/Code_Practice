#include <iostream>
using namespace std;

int main() {
    int n, x = 0;
    cin >> n;
    
    while (n != 1) {
        n /= 2;
        x++;
    }
    cout << x << endl;
    return 0;
}