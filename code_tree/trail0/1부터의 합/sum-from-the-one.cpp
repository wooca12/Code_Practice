#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int i;
    int sum = 0;
    for (i = 1; i <= 100; i++) {
        sum += i;
        if (sum >= n) 
            break;
    }
    cout << i;
    return 0;
}