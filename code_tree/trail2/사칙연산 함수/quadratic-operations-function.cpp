#include <iostream>
#include <string>
using namespace std;

void Cal(int a, char o, int b) {
    if (o == '+')
        printf("%d %c %d = %d", a, o, b, a + b);
    else if (o == '-') 
        printf("%d %c %d = %d", a, o, b, a - b);

    else if (o == '/')  
        printf("%d %c %d = %d", a, o, b, a / b);

    else if (o == '*')
        printf("%d %c %d = %d", a, o, b, a * b);
    else
        printf("False");
    
}

int main() {
    int a;
    int c;
    char o;
    cin >> a >> o >> c;
   
    Cal(a, o, c);
    

    return 0;
}