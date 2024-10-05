#include <iostream>
using namespace std;

void print_str(){
    cout << "12345^&*()_";
    cout << endl;
}

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for(int i ; i < n; i++){
        print_str();
    }  

    return 0;
}