#include <iostream>
using namespace std;

void ChangeEven(int n, int a[]) {
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0)
            a[i] /= 2;
    }
}
int main() {
    // Please write your code here.
    int n;
    int arr[100];

    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    ChangeEven(n, arr);


    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    
    return 0;
}