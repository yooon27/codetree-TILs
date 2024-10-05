#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, c, b ,d, ans, flag ;
    cin >> a >> b >> c >> d;
    if(b > d){
        ans = d - b + 60;
        flag = 1;
    }
    else ans = d - b;

    if(flag == 1) ans += (c-a-1)*60;
    else ans += (c-a) * 60;

    cout << ans;
    
    return 0;
}