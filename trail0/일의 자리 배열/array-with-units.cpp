#include <iostream>
using namespace std;

int main() {
    int arr[10];
    cin >> arr[0];
    cin >> arr[1];

    int i;
    for (i = 2; i < 10; i++)
        arr[i] = (arr[i - 2] + arr[i - 1]) % 10;
    
    for (i = 0; i < 10; i++)
        cout << arr[i] << " ";
    
    return 0;
}