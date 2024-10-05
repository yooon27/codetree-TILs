#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int m1, m2, d1, d2 , ans;
    cin >> m1 >> d1 >> m2 >> d2;

    if(m1 == m2){
        cout << d2-d1+1;
        return 0;
    }

    if(m1 == 1 || m1 == 3 || m1 == 5 || m1 == 7 || m1 == 8 || m1 == 10 ) ans = 31-d1;
    else if(m1 == 2) ans = 28 - d1;
    else ans = 30 - d1;

    m1+=1;
    while(m1 < m2){
        if(m1 == 1 || m1 == 3 || m1 == 5 || m1 == 7 || m1 == 8 || m1 == 10 ) ans += 31;
        else if(m1 == 2) ans += 28;
        else ans += 30;
        m1+=1;
    }
    
    ans += d2;
    cout << ans + 1;

    return 0;
}