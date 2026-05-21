#include <iostream>
using namespace std;
#define INIT_MAX 100

int main() {
    int n, nums[10];
    cin >> n;

    int min = INIT_MAX;

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int diff;
            
            
            if (nums[i] >= nums[j])
                diff = nums[i] - nums[j];
            else
                diff = nums[j] - nums[i];

            if (diff < min)
                min = diff;
        }
    }

    cout << min << endl;

    return 0;
}