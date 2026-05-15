#include <iostream>
using namespace std;

int main() {
    int start, end;
    cin >> start >> end;

    int cnt = 0, total = 0;
    for (int i = start; i <= end; i++) {
        cnt = 0;
        for (int j = 1; j <= i; j++) {
            if (i % j == 0)
                cnt++;
        }
        if (cnt == 3) 
            total++;
    }
    cout << total << endl;

    return 0;
}