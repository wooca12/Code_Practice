#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

#define MAX_N 100

int main() {
    int n;
    string arr[MAX_N];
    
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    std::sort(arr, arr + n);

    for (int i = 0; i < n; i++) {
        cout << arr[i] << endl;
    }
    return 0;
}