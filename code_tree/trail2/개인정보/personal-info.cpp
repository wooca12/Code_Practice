#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

class Person {
    public:
        string name;
        int height;
        double weight;

        Person(string name, int height, double weight) {
            this->name = name;
            this->height = height;
            this->weight = weight;
        }
        Person() {}
};

bool cmp_name(Person a, Person b) {
    return a.name < b.name;
}

bool cmp_height(Person a, Person b) {
    return a.height > b.height;
}
int main() {
    int n = 5;

    Person people[5];

    for (int i = 0; i < n; i++) {
        string name;
        int h;
        double w;
        cin >> name >> h >> w;

        people[i] = Person(name, h, w); 
    }

    cout << fixed;
    cout.precision(1);

    sort(people, people + n, cmp_name);

    cout << "name" << endl;
    for (int i = 0; i < n; i++) 
        cout << people[i].name << " " << people[i].height << " " << people[i].weight << endl;
    cout << endl; 

    sort(people, people + n, cmp_height);

    cout << "height" << endl;
    for (int i = 0; i < n; i++) 
        cout << people[i].name << " " << people[i].height << " " << people[i].weight << endl;


    return 0;
}