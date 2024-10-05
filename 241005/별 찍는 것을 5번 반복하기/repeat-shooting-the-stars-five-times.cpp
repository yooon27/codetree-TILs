#include <iostream>
using namespace std;

void print_5_stars(){
    for(int i = 0; i<10 ; i++)
        cout << "*";
    cout << endl;
}

int main() {
    for(int i = 0; i < 5; i++)
        print_5_stars();
    return 0;
}