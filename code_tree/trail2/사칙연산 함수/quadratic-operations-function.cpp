#include <iostream>
#include <string>
using namespace std;

int Plus(int a, int b) {
    return a + b;
}
int Minus(int a, int b) {
    return a - b;
}
int Times(int a, int b) {
    return a * b;
}
int Divide(int a, int b) {
    return a / b;
}


int main() {
    int a;
    int b;
    char o;
    cin >> a >> o >> b;
   
    if (o == '+')
        printf("%d %c %d = %d", a, o, b, Plus(a, b));
    else if (o == '-') 
        printf("%d %c %d = %d", a, o, b, Minus(a, b));
    else if (o == '/')  
        printf("%d %c %d = %d", a, o, b, Divide(a, b));
    else if (o == '*')
        printf("%d %c %d = %d", a, o, b, Times(a, b));
    else
        printf("False");
    

    return 0;
}