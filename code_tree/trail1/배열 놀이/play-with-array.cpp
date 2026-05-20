#include <iostream>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;

    int arr[100];

    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }
    for (int i = 0; i < q; i++) {
        int num;
        cin >> num;

        if (num == 1) {
            int a;
            cin >> a;
            cout << arr[a] << endl;
        }
        else if (num == 2) {
            int b, idx = 0;
            cin >> b;
            for (int j = 1; j <= n; j++) {
                if (arr[j] == b) {
                    idx = j;
                    break;
                }
            }
            cout << idx << endl;
        }
        else {
            int s, e;
            cin >> s >> e;
            for (int j = s; j <= e; j++) 
                cout << arr[j] << " ";
            cout << endl;
        }
    }
    return 0;
}