#include <iostream>
using namespace std;
#define MAX_N 100

int n, m;
int A[MAX_N];

int SumChangNum() {
    int sum = 0;

    while (m != 1) {
        sum += A[m - 1];
        if (m % 2 == 1)
            m -= 1;
        else
            m /= 2;
    }

    sum += A[m - 1];

    return sum;
}

int main() {
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    cout << SumChangNum();

    return 0;
}