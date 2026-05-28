#include <iostream>

using namespace std;


int Num(int a, int b) {
    int answer = 1;
    for (int i = 1; i <= b; i++) {
        answer *= a;
    }
    return answer;
}
int main() {
    int a, b;
    cin >> a >> b;

    cout << Num(a, b) << endl;

    return 0;
}