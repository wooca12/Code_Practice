#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
//      0 1 2 3 4 5
//   0  * * * * * * &
//   1    *   *   * -
//   2        *   * &
//   3        *   * -
//   4            * &
//   5            * - 
 
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == 0)
                cout << "* ";
            else if ((i <= j) && (j % 2 == 1))
                cout << "* ";
            else
                cout << "  ";
        }
        cout << endl;
    }
    return 0;
}