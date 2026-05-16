#include <iostream>
using namespace std;

int main() {
    int a_age;
    char a_gen;
    int b_age;
    char b_gen;

    cin >> a_age >> a_gen;
    cin >> b_age >> b_gen;
    
    if ((a_age >= 19) && (a_gen == 'M') || (b_age >= 19) && (b_gen == 'M'))
        cout << 1 << endl;
    else    
        cout << 0 << endl;
    return 0;
}