#include <iostream>

using namespace std;

#define MAX_N 20

int a, b;
string n;

int main() {
    cin >> a >> b;
    cin >> n;

    int num = 0;
    
    for (int i = 0; i < n.length(); i++) {
        num = num * a + n[i] - '0';
    }
    
    int arr[MAX_N];
    int cnt = 0;

    while (true) {
        if (num < b) {
            arr[cnt++] = num;
            break;
        }
        arr[cnt++] = num % b;
        num /= b;
    }

    for (int i = cnt - 1; i >= 0; i--) {
        cout << arr[i];
    }



    return 0;
}