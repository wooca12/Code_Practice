#include <iostream>
#include <string>
using namespace std;
#define MAX_N 1000000000

int ToDecimal(string str) {
    int num = 0;

    for (int i = 0; i < str.length(); i++) {
        num = num * 2 + (str[i] - '0');
    }
    return num;
}

string ToBinary(int num) {
    int arr[MAX_N];
    int cnt = 0;

    while (true) {
        if (num < 2) {
            arr[cnt++] = num;
            break;
        }
        arr[cnt++] = num % 2;
        num /= 2;
    }

    string a = "";
    for (int i = cnt - 1; i >= 0; i--) {
        a += to_string(arr[i]);
    }

    return a;
}
int main() {
    string str;
    cin >> str;

    int d = ToDecimal(str);
    d *= 17;
    string s = ToBinary(d);

    cout << s << endl;

    
    return 0;
}