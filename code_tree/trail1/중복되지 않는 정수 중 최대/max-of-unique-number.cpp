#include <iostream>
#include <climits>
using namespace std;

int main() {
    int n;
    cin >> n;

    int cnt[1001] = {};
    int max_val = -1;

    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;

        cnt[num]++;
    }
    
    
    for (int i = 1; i < 1001; i++) {
        if (cnt[i] == 1 && max_val < i)
            max_val = i;
    }

    cout << max_val << endl;


    return 0;
}