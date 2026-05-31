#include <iostream>
#include <string>
using namespace std;

class Secret {
    public:
        string code;
        char point;
        int time;

        Secret(string code, char point, int time) {
            this->code = code;
            this->point = point;
            this->time = time;
        }
};


int main() {
    string code;
    char point;
    int time;
    
    cin >> code >> point >> time;

    Secret secret = Secret(code, point, time);

    cout << "secret code : " << secret.code << endl;
    cout << "meeting point : " << secret.point << endl;
    cout << "time : " << secret.time << endl;
    
    return 0;
}