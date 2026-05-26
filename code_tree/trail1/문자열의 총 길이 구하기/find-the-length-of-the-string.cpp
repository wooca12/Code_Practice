#include <iostream>
#include <string>
using namespace std;

int main() {
    int n = 10;
    string arr[10];

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < arr[i].length(); j++)
            count++;
    }
    cout << count << endl;
    return 0;
}