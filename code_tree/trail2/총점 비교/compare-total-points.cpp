#include <iostream>
#include <algorithm>
#include <string>
#define MAX_N 10
using namespace std;

class Student {
    public:
        string name;
        int score1, score2, score3;

        Student(string name, int score1, int score2, int score3) {
            this->name = name;
            this->score1 = score1;
            this->score2 = score2;
            this->score3 = score3;
        }
        Student() {}
};

bool cmp(Student a, Student b) {
    return a.score1 + a.score2 + a.score3 < b.score1 + b.score2 + b.score3;
}

int main() {
    int n;
    cin >> n;

    Student students[MAX_N];

    for (int i = 0; i < n; i++) {
        string name;
        int s1, s2, s3;
        cin >> name >> s1 >> s2 >> s3;

        students[i] = Student(name, s1, s2, s3);
    }

    sort(students, students + n, cmp);

    for (int i = 0; i < n; i++) {
        cout << students[i].name << " " << students[i].score1 << " " << students[i].score2 << " " << students[i].score3 << endl;
    }
    return 0;
}