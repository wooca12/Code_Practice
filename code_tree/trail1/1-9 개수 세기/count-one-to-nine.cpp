#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[100];
    int cout_arr[10] = {};

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        cout_arr[arr[i]]++;
    }
    for (int i = 1; i < 10; i++) {
        cout << cout_arr[i] << endl;
    }
    return 0;
}