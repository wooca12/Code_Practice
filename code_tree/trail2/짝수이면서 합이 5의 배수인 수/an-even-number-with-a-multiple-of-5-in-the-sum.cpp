#include <iostream>
using namespace std;

bool Num5(int n) {
    int sum = (n / 10) + (n % 10);
    return (n % 2 == 0 && sum % 5 == 0);
}
int main() {
    int n;
    cin >> n;

    if (Num5(n)) 
        cout << "Yes";
    else
        cout << "No";
    return 0;
}