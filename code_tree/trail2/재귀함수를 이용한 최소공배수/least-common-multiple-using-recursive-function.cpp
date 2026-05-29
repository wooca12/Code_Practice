#include <iostream>

using namespace std;

int n;
int arr[10];

bool IsPrime(int n) {
    for (int i = 2; i < n; i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}

int GetGcd(int a, int b) {
    int ans;
    for (int i = 1; i <= min(a, b); i++) {
        if (a % i == 0 && b % i == 0)
            ans = i;
    }
    return ans;

}

int GetLcm(int a, int b) {
    int gcd = GetGcd(a, b);

    return ((a * b) / gcd);
}

int GetTotalLcm(int n) {
    if (n == 0)
        return arr[0];
    return GetLcm(arr[n], GetTotalLcm(n - 1));
}


int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << GetTotalLcm(n - 1);

    return 0;
}