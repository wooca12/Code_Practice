#include <iostream>
using namespace std;
#define INIT_MAX 1000

int main() {
    int n;
    cin >> n;

    int costs[INIT_MAX];

    for (int i = 0; i < n; i++) {
        cin >> costs[i];
    }
     
    int max = 0;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int diff = costs[j] - costs[i];

            if (diff > max)
                max = diff;
        }
    }

    cout << max << endl;
    
    return 0;
}