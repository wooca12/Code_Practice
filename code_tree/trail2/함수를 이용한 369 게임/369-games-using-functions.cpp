#include <iostream>
using namespace std;

bool isNum3(int num) {
    while (num > 10) { 
        int m = num % 10;
        if (m == 3 || m == 6 || m == 9) {
            return true;
        }
        num /= 10;
    }
    return (num % 3 == 0);
}

bool isMagicNum(int n) {
    return (isNum3(n) || n % 3 == 0);
}

int main() {
    int a, b;
    cin >> a >> b;

    int cnt = 0;
    for (int i = a; i <= b; i++) {
        if (isMagicNum(i))
            cnt++;
    }   

    cout << cnt << endl;

    return 0;
}