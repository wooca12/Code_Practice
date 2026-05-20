#include <iostream>
using namespace std;

int main() {
    char arr[6] = {'L', 'E', 'B', 'R', 'O', 'S'};
    char x;
    cin >> x;

    int idx = -1;
    for (int i = 0; i < 6; i++) {
        if (arr[i] == x)
            idx = i;
    }
    if (idx == -1)
        cout << "None" << endl;
    else
        cout << idx << endl;

    return 0;
}