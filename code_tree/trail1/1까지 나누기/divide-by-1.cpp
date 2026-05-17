#include <iostream>
using namespace std;

int main() {
    int n, a, cnt = 0;
    cin >> n;
    
    a = n;
    for (int i = 1; i <= n; i++) {
        a /= i;
        cnt++; 
        if (a <= 1) 
            break;
        
    }
    cout << cnt << endl;
    return 0;
}