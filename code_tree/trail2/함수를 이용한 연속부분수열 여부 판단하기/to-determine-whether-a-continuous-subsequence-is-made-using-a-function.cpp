#include <iostream>

using namespace std;

// bool IsSatisfied(int n1, int a[], int n2, int b[]) {
//     bool satisfied;

//     for (int i = 0; i < n1; i++) {
//         satisfied = true;
//         for (int j = 0; j < n2; j++) {
//             if (a[i + j] != b[j])
//                 satisfied = false;
//         }
//         if (satisfied)
//             return true;
//     } 
//     return false;
// }

bool IsSame(int idx, int a[], int n2, int b[]) {
    for (int i = 0; i < n2; i++) {
        if (a[idx + i] != b[i])
            return false;
    }
    return true;
}

int IsSubSequence(int n1, int a[], int n2, int b[]) {
    for (int i = 0; i <= n1 - n2; i++) {
        if (IsSame(i, a, n2, b))
            return true;
    }
    return false;
}

int main() {
    int n1, n2;
    int a[100], b[100];
    cin >> n1 >> n2;

    for (int i = 0; i < n1; i++) 
        cin >> a[i];
    for (int i = 0; i < n2; i++) 
        cin >> b[i];

    // if (IsSatisfied(n1, a, n2, b))
    //     cout << "Yes" << endl;
    // else 
    //     cout << "No" << endl;

    if (IsSubSequence(n1, a, n2, b))
        cout << "Yes" << endl;
    else 
        cout << "No" << endl;




    

    return 0;
}