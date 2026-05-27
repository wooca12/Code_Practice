#include <iostream>
#include <string>
using namespace std;

int main() {
    string in_s;
    string obj_s;
    
    cin >> in_s >> obj_s;

    int idx = in_s.find(obj_s);

    cout << idx << endl;
    return 0;
}