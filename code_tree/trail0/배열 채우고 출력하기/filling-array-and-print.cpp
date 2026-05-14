#include <iostream>
using namespace std;

int main() {
    char a[10];
    int i;

    for (i = 0; i < 10; i++)
        cin >> a[i];
    
    for (i = 9; i >= 0; i--)
        cout << a[i];
    return 0;
}