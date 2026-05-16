#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    
    if (N >= 3000)
        cout << "book" << endl;
    else if (N >= 1000)
        cout << "mask" << endl;
    else if (N >= 500)
        cout << "pen" << endl;
    else
        cout << "no" << endl;
    return 0;
}