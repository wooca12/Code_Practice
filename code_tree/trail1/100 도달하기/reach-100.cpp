#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int pp = 1;
    int p = n;

    cout << pp << " " << p << " ";
    for (int i = 2; i < 100; i++) {
        int temp = p + pp;
        pp = p;
        p = temp;

        cout << p << " ";
        if (p > 100)
            break;
    }
    return 0;
}