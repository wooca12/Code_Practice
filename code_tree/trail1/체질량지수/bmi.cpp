#include <iostream>
using namespace std;

int main() {
    int h, w;
    cin >> h >> w;

    int b = (double)(10000 * w) / (h * h);

    cout << fixed;
    cout.precision(1);
    cout << b << endl;

    if (b >= 25) 
        cout << "Obesity" << endl;

    return 0;
}