#include <iostream>
#include <algorithm>
#define MAX_N 100
using namespace std;

int main() {
    int n;
    int arr[MAX_N];

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n);

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;


    sort(arr, arr + n, greater<int>());
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;




    return 0;
}