#include <iostream>
using namespace std;

bool IsSatisfied(int n) {
    
    if (n % 2 == 0)
        return false;
    if (n % 10 == 5)
        return false;
    if (n % 3 == 0 && n % 9 != 0)
        return false;
    return true;
}

int main() {
    int a, b;
    cin >> a >> b;

    int count = 0;

    for (int i = a; i <= b; i++) {
        if (IsSatisfied(i))
            count++;
    }

    cout << count << endl;


    return 0;
}