#include <iostream>

using namespace std;

int n;
int arr[100];

// int FindMax(int max, int n) {
//     if (n == -1) {
//         return max;
//     }
//     if (max < arr[n]) {
//         return FindMax(arr[n], n - 1);
//     }
//     else {
//         return FindMax(max, n - 1);
//     }    
// }

int FindMax(int a) {
    if (a == 0)
        return arr[0];
    
    return max(FindMax(a - 1), arr[a]);
}

int main() {
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << FindMax(n - 1);

    

    return 0;
}