#include <iostream>
#include <algorithm>
#include <cmath>
#define MAX_N 1000
using namespace std;

class Point {
    public:
        int num, x, y;

        Point(int num, int x, int y) {
            this->num = num;
            this->x = x;
            this->y = y;
        }
        Point() {}
};

bool cmp(Point a, Point b) {
    int d1 = abs(a.x) + abs(a.y);
    int d2 = abs(b.x) + abs(b.y);
    
    if (d1 != d2)   
        return d1 < d2;
    return a.num < b.num;
}

int main() {
    int n;
    cin >> n;

    Point points[MAX_N];

    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;

        points[i] = Point((i + 1), x, y);
    }

    sort(points, points + n, cmp);

    for (int i = 0; i < n; i++) {
        cout << points[i].num << endl;
    }
    return 0;
}