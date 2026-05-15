#include <iostream>
using namespace std;

int main() {
    string S, T;
    string tmp;
    cin >> S >> T;
    
    tmp = S;
    S = T;
    T = tmp;

    cout << S << "\n" << T << endl;

    return 0;
}