#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;

    int sum = 0;
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        sum += num;
    }

    string n_str = to_string(sum);
    int len = n_str.length();

    n_str = n_str.substr(1, len - 1) + n_str.substr(0, 1);

    cout << n_str << endl;
    return 0;
}