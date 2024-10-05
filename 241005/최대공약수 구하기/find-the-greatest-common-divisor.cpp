#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n, m ,number;
    cin >> n >> m;
    if(n>m){
        number = m;
    }
    else{
        number = n;
    }

    while(number > 0){
        if(n%number == 0 && m % number == 0){
            break;
        }
        number -= 1;
    }
    cout << number;

    return 0;
}