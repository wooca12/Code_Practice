#include <iostream>
using namespace std;

int main() {
    int h1, m1, h2, m2;
    cin >> h1 >> m1;
    cin >> h2 >> m2;

    // int answer = 0;
    // int min = 0, hour = 0;

    // while(true) {
    //     if (h1 == h2 && m1 == m2) 
    //         break;

    //     answer++;
    //     m1++;
    //     if (m1 == 60) {
    //         h1++;
    //         m1 = 0;
    //     }
    // }

    int answer = (h2 * 60 + m2) - (h1 * 60 + m1);

    cout << answer << endl;

    return 0;
}