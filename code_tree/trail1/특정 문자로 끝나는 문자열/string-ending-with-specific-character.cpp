#include <iostream>
#include <string>
using namespace std;

int main() {
    int n = 10;
    string arr[10];
    
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    char c;
    cin >> c;

    bool flag = false;
    for (int i = 0; i < n; i++) {
        int idx = arr[i].length() - 1;
        if (arr[i][idx] == c) {
            cout << arr[i] << endl;
            flag = true;
        }
    }
    if (flag)
        return 0;
    else    
        cout << "None" << endl;
}