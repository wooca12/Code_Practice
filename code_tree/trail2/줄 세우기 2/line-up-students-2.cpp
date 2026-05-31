#include <iostream>
#include <algorithm>
#define MAX_N 1000
using namespace std;

class Student {
    public:
        int height, weight, number;

        Student(int height, int weight, int number) {
            this->height = height;
            this->weight = weight;
            this->number = number;
        }

        Student() {}
};

bool cmp(Student a, Student b) {
    if (a.height != b.height)
        return a.height < b.height;
    return a.weight > b.weight;
}

int main() {
    int n, cache_h, cache_w;
    cin >> n;

    Student students[MAX_N];

    for (int i = 0; i < n; i++) {
        cin >> cache_h >> cache_w;

        students[i] = Student(cache_h, cache_w, i + 1);
    }

    sort(students, students + n, cmp);

    for (int i = 0; i < n; i++) {
        cout << students[i].height << " " << students[i].weight << " " << students[i].number << endl;
    }


    return 0;
}