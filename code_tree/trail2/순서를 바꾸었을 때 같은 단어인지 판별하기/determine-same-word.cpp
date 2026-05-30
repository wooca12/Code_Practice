#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    if (a == b) 
        cout << "Yes";
    else
        cout << "No";

    return 0;
}