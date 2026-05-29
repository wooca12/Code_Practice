#include <iostream>
using namespace std;

void PrintNumSorted(int n) {
    if (n == 0)
        return;

    PrintNumSorted(n - 1);
    cout << n << " ";
    
}
void PrintNumReversed(int n) {
    if (n == 0)
        return;

    cout << n << " ";
    PrintNumReversed(n - 1);
    
}

int main() {
    int n;
    cin >> n;

    PrintNumSorted(n);

    cout << endl;

    PrintNumReversed(n);

    return 0;
}