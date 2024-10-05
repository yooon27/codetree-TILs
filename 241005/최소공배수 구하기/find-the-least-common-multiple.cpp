#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n , m , number;
    cin >> n >> m;
    
    if(n>m) number = m;
    else number = n;

    for(int i = number ; i > 0 ; i--){
        if(n%i == 0 && m%i == 0) {
            number = i;
            break;}

    }

    cout << (number * (n/number) * (m/number));

    return 0;
}