#include <iostream>
using namespace std;

int main() {
    char y1, y2, y3;
    int n1, n2, n3;

    cin >> y1 >> n1;
    cin >> y2 >> n2;
    cin >> y3 >> n3;

    if ((y1 == 'Y' && n1 >= 37) && ((y2 == 'Y' && n2 >= 37) || (y3 == 'Y' && n3 >= 37)))
        cout << "E" << endl;
    else if ((y2 == 'Y' && n2 >= 37) && (y3 == 'Y' && n3 >= 37))
        cout << "E" << endl;
    else
        cout << "N" << endl;

    return 0;
}