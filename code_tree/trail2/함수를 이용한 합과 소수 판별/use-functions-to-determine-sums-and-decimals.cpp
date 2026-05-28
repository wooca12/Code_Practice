#include <iostream>
using namespace std;

bool IsPrime(int num) {
    for (int i = 2; i < num; i++) {
        if (num % i == 0)
            return false;
    }
    return true;
}

bool IsSumEven(int num) {
    int sum = 0;

    while (num >= 10) {
        int t = num % 10;
        sum += t;
        num /= 10;
    }
    sum += num;
    
    return (sum % 2 == 0);

}

int main() {
    int a, b;
    cin >> a >> b;

    int cnt = 0;

    for (int i = a; i <= b; i++) {
        if (IsPrime(i) && IsSumEven(i))
            cnt++;
    }
    cout << cnt << endl;
    
    return 0;
}