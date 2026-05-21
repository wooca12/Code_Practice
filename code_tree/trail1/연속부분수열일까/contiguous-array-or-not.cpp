#include <iostream>
using namespace std;

int main() {
    int n1, n2;
    cin >> n1 >> n2;

    int a[100], b[100];
    
    for (int i = 0; i < n1; i++) 
        cin >> a[i];
    for (int j = 0; j < n2; j++) 
        cin >> b[j];

    
    for (int i = 0; i < n1; i++) {
        bool success = true;
        
        for (int j = 0; j < n2; j++) {
            if (i + j >= n1) { // a 범위 밖
                success = false;
                break;
            }
            if(a[i + j] != b[j]) {
                success = false;
                break;
            }
        }
        if(success) {
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}