#include <iostream>
using namespace std;

int main() {
    int score;
    cin >> score;

    string level = score == 100 ? "pass" : "failure";

    cout << level << endl;
    
    return 0;
}