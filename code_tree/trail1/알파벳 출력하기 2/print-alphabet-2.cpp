#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    char x = 'A';
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            cout << "  ";
        }
        for (int j = i; j < n; j++) {
            cout << x << " ";
            x++;
            if (x > 'Z')
                x = 'A';
        }
        cout << endl;
    }
    return 0;
}