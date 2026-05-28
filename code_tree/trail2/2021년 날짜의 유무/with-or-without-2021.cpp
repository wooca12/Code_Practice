#include <iostream>
using namespace std;

bool IsExistDay(int m, int d) {
    if (m < 1 or m > 12)
        return false;
    
    int arr[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    return d <= arr[m];
}
int main() {
    int m, d;
    cin >> m >> d;
    
    if (IsExistDay(m, d)) 
        cout << "Yes";
    
    else
        cout << "No";

    return 0;
}