#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    int n;

    cin >> str >> n;

    int len = n < str.length() ? n : str.length();
    
    for (int i = 0; i < len; i++) {
        cout << str[str.length() - i - 1];
    }

    return 0;
}