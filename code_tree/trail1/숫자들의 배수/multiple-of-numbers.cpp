#include <iostream>
using namespace std;

int main() {
    int n, prod = 0;
    cin >> n;

    int cnt = 0;

    while (cnt != 2) {
        prod += n;
        cout << prod << " ";
        if (prod % 5 == 0)
            cnt++;
    }
    return 0;
}