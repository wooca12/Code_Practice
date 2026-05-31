#include <iostream>
#include <algorithm>
#define MAX_N 1000
#define MAX_NUMBER 1000001
using namespace std;

class Number {
    public:
        int index, number;
        
        Number (int index, int number) {
            this->index = index;
            this->number = number;
        }
        Number() {}
};

bool cmp (Number a, Number b) {
    if (a.number != b.number)
        return a.number < b.number;
    return a.index < b.index;
} 

int main() {
    int n, num;
    cin >> n;

    Number numbers[MAX_N];
    int answer[MAX_N];

    for (int i = 0; i < n; i++) {
        cin >> num;
        numbers[i] = Number(i, num);
    }

    sort(numbers, numbers + n, cmp);

    for (int i = 0; i < n; i++) {
        answer[numbers[i].index] = i + 1;
    }

    for (int i = 0; i < n; i++) {
        cout << answer[i]<< " ";
    }
    return 0;
}