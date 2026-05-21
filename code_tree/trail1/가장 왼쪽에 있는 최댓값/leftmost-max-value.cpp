#include <iostream>
#include <climits>
using namespace std;
#define MAX_N 1000

int main() {
    int n, nums[MAX_N];

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    int end = n;

    while (true) {
        if (end == 0)
            break;

        int max = INT_MIN;
        

        for (int i = 0; i < end; i++) {
            if (max < nums[i]) {
                max = nums[i];
            }
        }

        for (int i = 0; i < end; i++) {
            if (max == nums[i]) {
                end = i;
                break;
            }
        }

        cout << end + 1 << " ";
    }

    return 0;
}