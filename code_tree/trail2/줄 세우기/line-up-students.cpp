#include <iostream>
#include <algorithm>
#define MAX_N 1000
using namespace std;

class Student {
    public:
        int number, height, weight;

        Student(int number, int height, int weight) {
            this->number = number;
            this->height = height;
            this->weight = weight;
        }
        Student() {};
};

bool cmp(Student a, Student b) {
    if (a.height != b.height)
        return a.height > b.height;
    if (a.weight != b.weight)
        return a.weight > b.weight;
    return a.number < b.number;
}
    
int main() {
    int n;
    cin >> n;

    Student students[MAX_N];

    for (int i = 0; i < n; i++) {
        int h, w;
        cin >> h >> w;

        students[i] = Student(i + 1, h, w);
    }

    sort(students, students + n, cmp);

    for (int i = 0; i < n; i++) {
        cout << students[i].height << " " << students[i].weight << " " << students[i].number << endl;
    }

    return 0;
}