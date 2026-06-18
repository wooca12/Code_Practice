#include <iostream>
#define MAX_N 9
using namespace std;


int main() {
    char binary[MAX_N];
    cin >> binary;

    int num = 0;

    for (int i = 0; binary[i] != '\0' ; i++) {
        num = num * 2 + int(binary[i] - '0');
    }

    cout << num << endl;


    return 0;
}