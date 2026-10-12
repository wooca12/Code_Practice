#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    int i;
    for (i = b; i >= a; i--)
        cout << i << " ";
    
    return 0;
}