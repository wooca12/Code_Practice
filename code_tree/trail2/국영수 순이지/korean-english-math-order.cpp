#include <iostream>
#include <tuple>
#include <algorithm>
#include <string>
#define MAX_N 10 

using namespace std;

int main() {
    int n;
    cin >> n;

    tuple <int, int, int, string> students[MAX_N];

    for (int i = 0; i < n; i++) {
        string name;
        int sc1, sc2, sc3;
        cin >> name >> sc1 >> sc2 >> sc3;
        students[i] = make_tuple(-sc1, -sc2, -sc3, name);
    }

    sort(students, students + n);

    for (int i = 0; i < n; i++) {
        string name;
        int s1, s2, s3;
        tie(s1, s2, s3, name) = students[i];
        cout << name << " " << -s1 << " " << -s2 << " " << -s3 << endl;
    }
    return 0;
}