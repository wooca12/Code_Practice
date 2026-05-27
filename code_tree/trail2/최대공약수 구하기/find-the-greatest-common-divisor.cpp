#include <iostream>

using namespace std;

void PrintMaxNum(int n, int m) {
    int max = 0;
    int last = n > m ? n : m;
    for (int i = 1; i <= last; i++) {
        if ((n % i == 0) && (m % i == 0))
            max = i;
    }
    cout << max << endl;
}

int main() {
    int n, m;
    cin >> n >> m;

    PrintMaxNum(n, m);

    return 0;
}