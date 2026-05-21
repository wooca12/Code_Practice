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

    int idx = 0;
    bool satisfied = false;
    
    for (int i = 0; i < n1; i++) {
        if (a[i] == b[idx]) {
            satisfied = true;
            for (int j = 0; j < n2; j++) {
                if (a[i] == b[j]) {
                    i++;
                }
                else {
                    satisfied = false;
                    break;
                }
            }
            if (satisfied)
                break;
        }
    }
    if (satisfied)
        cout << "Yes" << endl;
    else
        cout << "No" << endl;
    
    return 0;
}