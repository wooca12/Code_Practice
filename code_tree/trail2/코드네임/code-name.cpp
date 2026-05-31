#include <iostream>
#include <tuple>
#include <string>
using namespace std;

class Employee {
    public:
        string code_name;
        int score;

        Employee(string code_name, int score) {
            this->code_name = code_name;
            this->score = score;
        }
        Employee() {}

};

int main() {
    int n = 5;
    Employee users[5];

    for (int i = 0; i < n; i++) {
        string name;
        int score;
        cin >> name >> score;

        users[i] = Employee(name, score);
    }

    int min_idx = 0;    
    for (int i = 1; i < n; i++) {
        if (users[min_idx].score > users[i].score)
            min_idx = i;
    }
    cout << users[min_idx].code_name << " " << users[min_idx].score;

    return 0;
}