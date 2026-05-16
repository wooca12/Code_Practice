#include <iostream>
using namespace std;

int main() {
    int s1, s2;
    cin >> s1 >> s2;

    if (s1 >= 90 && s2 >= 95)
        cout << 100000 << endl;
    else if (s1 >= 90 && s2 >= 90)
        cout << 50000 << endl;
    else
        cout << 0 << endl;


    return 0;
}