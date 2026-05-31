#include <iostream>
#include <algorithm>
#define MAX_N 1000
#define MAX_NUMBER 1000001
using namespace std;

class Number {
    public:
        int id, number;
        
        Number (int id, int number) {
            this->id = id;
            this->number = number;
        }
        Number() {}
};

bool cmp (Number a, Number b) {
    if (a.number != b.number)
        return a.number < b.number;
    return a.id < b.id;
} 
int main() {
    int n;
    cin >> n;

    Number arr1[MAX_N];
    Number arr2[MAX_N];

    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;

        arr1[i] = Number(i + 1, num);
        arr2[i] = Number(0, num);

    }

    sort(arr1, arr1 + n, cmp);

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (arr1[i].number == arr2[j].number) {
                if (arr2[j].id == 0) {
                    arr2[j].id = i + 1;
                    break;
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << arr2[i].id << " ";
    }
    return 0;
}