#include <iostream>
using namespace std;

int main() {
    int a, b, i;
    cin >> a >> b;
    
    i = a;
    while (i <= b) {
        cout << i << " ";
        if (i % 2 == 1)
            i *= 2;
        else
            i += 3; 
    }

    return 0;
}