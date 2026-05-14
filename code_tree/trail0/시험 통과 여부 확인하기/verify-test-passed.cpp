#include <iostream> 
using namespace std;

int main() {
    int a;
    cin >> a;

    if (a >= 80) cout << "pass" << endl;
    else cout << 80 - a << " more score" << endl;
    
    return 0;
}