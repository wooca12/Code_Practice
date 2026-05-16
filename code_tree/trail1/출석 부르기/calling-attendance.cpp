#include <iostream>
using namespace std;

int main() {
    int num;
    cin >> num;

    if (num == 1) 
        cout << "John" << endl;
    else if (num == 2)
        cout << "Tom" << endl;
    else if (num == 3)
        cout << "Paul" << endl;
    else
        cout << "Vacancy" << endl;
    return 0;
}