#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        int prod_val = 1;
        for (int j = a; j <= b; j++) {
            prod_val *= j;
        }
        cout << prod_val << endl;

    }
    return 0;
}