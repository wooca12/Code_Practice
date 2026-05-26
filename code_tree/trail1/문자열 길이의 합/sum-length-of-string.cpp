#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    string arr[10];

    for (int i = 0 ; i < n; i++) {
        cin >> arr[i];
    }
    
    int cnt = 0;
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i].length();
        if (arr[i][0] == 'a')
            cnt++;
    }
    cout << sum << " " << cnt << endl;
    return 0;
}