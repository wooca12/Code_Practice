#include <iostream>
using namespace std;

int main() {
    int n;
    char x = 'A';
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cout << x;
            x++;
            if (x > 'Z')
                x = 'A';
        }
        cout << endl;
    }
    
    return 0;
}