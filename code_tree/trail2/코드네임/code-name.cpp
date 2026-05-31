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
    Employee employees[5];

    for (int i = 0; i < n; i++) {
        cin >> employees[i].code_name >> employees[i].score;
    }

    tuple <string, int> min_score = make_tuple("-1", 1000);
    
    for (int i = 0; i < n; i++) {
        if (get<1>(min_score) > employees[i].score)
            min_score = make_tuple(employees[i].code_name, employees[i].score);
    }

    cout << get<0>(min_score) << " " << get<1>(min_score);

    return 0;
}