#include <iostream>
#include <string>
using namespace std;


class User {
    public:
    
    string id;
    int lv;

    User(string id = "codetree", int lv = 10) {
        this->id = id;
        this->lv = lv;
    }

};

int main() {
    string id;
    int lv;

    cin >> id >> lv;

    User us1 = User();
    User us2 = User(id, lv);

    cout << "user " << us1.id << " lv " << us1.lv << endl;
    cout << "user " << us2.id << " lv " << us2.lv << endl;
 




    return 0;
}