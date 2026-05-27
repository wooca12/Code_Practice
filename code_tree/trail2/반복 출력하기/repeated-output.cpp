#include <iostream>
using namespace std;

void PrintNLines(int n) {
    for (int i = 0; i < n; i++) {
        cout << "12345^&*()_" << endl;
    }
}
int main() {
    int n_row;
    cin >> n_row;

    PrintNLines(n_row);

    return 0;
}