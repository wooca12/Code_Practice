#include <iostream>
#include <climits>
using namespace std;

int main() {
    int n; 
    cin >> n;
    
    int arr[100];

    int max1 = 0, max2 = 0;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];

        if (arr[i] > arr[max1])
            max1 = i;
    }
     
    for (int i = 0; i < n; i++) {
        if (max1 == max2) {
            max2 = i;
        }
        if (max1 == i)
            continue;
        if (arr[i] > arr[max2]) 
            max2 = i;
    }
    
    cout << arr[max1] << " " << arr[max2] << endl;

    return 0;
}