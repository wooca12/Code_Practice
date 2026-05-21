#include <iostream>
#include <climits>
using namespace std;

int main() {
    int max = INT_MIN;

    for (int i = 0; i < 10; i++) {
        int num;
        cin >> num;

        if(max < num) 
            max = num;
        
    }
    cout << max << endl;
    
    return 0;
}