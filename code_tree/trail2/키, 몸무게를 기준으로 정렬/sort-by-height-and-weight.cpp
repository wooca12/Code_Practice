#include <iostream>
#include <string>
#include <algorithm>
#define MAX_N 10
using namespace std;

class Info {
    public:
        string name;
        int height, weight;

        Info(string name, int height, int weight) {
            this->name = name;
            this->height = height;
            this->weight = weight;
        }
        Info() {}
};

bool cmp (Info a, Info b) {
    if (a.height != b.height)
        return a.height < b.height;
    if (a.weight != b.weight)
        return a.weight > b.weight;
}

int main() {
    int n;
    cin >> n;

    Info infos[MAX_N];
    for (int i = 0; i < n; i++) {
        string name;
        int h, w;
        cin >> name >> h >> w;

        infos[i] = Info(name, h, w);
    }

    sort(infos, infos + n, cmp);

    for (int i = 0; i < n; i++) {
        cout << infos[i].name << " " << infos[i].height << " " << infos[i].weight << endl;
    }

    

    return 0;
}