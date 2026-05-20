#include <iostream>
using namespace std;

int main() {
    int cnt[10] = {};
    int arr[100];
    for (int i = 0; i < 100; i++) {
        cin >> arr[i];

        if (arr[i] == 0)
            break;
        if (arr[i] >= 10) {
            cnt[arr[i] / 10]++;
        }
    }
    for (int i = 1; i < 10; i++) 
        cout << i << " - " << cnt[i] << endl;
    return 0;
}