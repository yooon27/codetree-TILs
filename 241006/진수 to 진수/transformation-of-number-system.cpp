#include <iostream>
using namespace std;
#include <string>
#include <algorithm>
#include <cmath>
int main() {
    // 여기에 코드를 작성해주세요.
    int a, b, n;
    cin >> a >> b;
    cin >> n;

    int decimal = 0 , i = 0;
    while(n > 0){
        decimal += (n%10)*pow(a,i);
        n = (int)(n/10);
        i++;
    }
    string str = "";
    while(decimal > 0){
        str += to_string(decimal%b);
        decimal = (int)(decimal/b);
    }

    reverse(str.begin(), str.end());
    cout << str;
    

    return 0;
}