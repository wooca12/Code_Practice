#include <iostream>
using namespace std;

int Num(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum / 10; 
}

int main() {
    int n;
    cin >> n;

    int ans = Num(n);
    cout << ans << endl;
    
    return 0;
}