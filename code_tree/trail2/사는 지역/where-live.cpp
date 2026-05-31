#include <iostream>
#include <string>
#define MAX_N 10

using namespace std;

class Info {
    public:
        string name, number, city;

        Info(string name, string number, string city) {
            this->name = name;
            this->number = number;
            this->city = city;
        }
        Info() {}
} ;


int main() {
    int n;
    cin >> n;

    Info infos[MAX_N];

    for (int i = 0; i < n; i++) {
        string name, number, city;
        cin >> name >> number >> city;

        infos[i] = Info(name, number, city);
    }

    int last_idx = 0;
    for (int i = 1; i < n; i++) {
        if (infos[last_idx].name < infos[i].name)
            last_idx = i;
    }

    cout << "name " << infos[last_idx].name << endl;
    cout << "addr " << infos[last_idx].number << endl;
    cout << "city " << infos[last_idx].city << endl;


    return 0;
}