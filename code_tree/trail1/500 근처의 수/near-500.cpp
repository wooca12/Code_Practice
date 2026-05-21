#include <iostream>
using namespace std;
#define INIT_MAX 1000
#define INIT_MIN 1

int main() {
    int nums[10];
    int max = INIT_MIN, min = INIT_MAX;

    for (int i = 0; i < 10; i++) {
        cin >> nums[i];

        if (nums[i] < 500 && max < nums[i])
            max = nums[i];
        if (nums[i] > 500 && min > nums[i])
            min = nums[i];
    }

    cout << max << " " << min << endl;
    return 0;
}