#include <iostream>
#include <string>
using namespace std;

int main() {
    string str;
    getline(cin, str);

    for (int i = 2; i < 10; i++) {
        printf("%c", str[i]);
    }

    return 0;
}