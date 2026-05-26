#include <iostream>
#include <string>

using namespace std;

string A;

int main() {
    cin >> A;
    string new_A = "";

    char cur_char = A[0];
    int num_char = 1;

    int idx = -1;
    for (int i = 1; A[i] != '\0'; i++) {
        if (cur_char == A[i]) {
            num_char++;
        }
        else {
            new_A += cur_char;
            new_A += to_string(num_char);
            cur_char = A[i];
            num_char = 1;
        }
    }
    new_A += cur_char;
    new_A += to_string(num_char);
    
    cout << new_A.length() << endl;
    cout << new_A << endl;
    return 0;
}
