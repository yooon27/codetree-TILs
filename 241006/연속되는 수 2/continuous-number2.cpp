#include <iostream>
using namespace std;
#include <algorithm>
int main() {
    // 여기에 코드를 작성해주세요.
    int n , prev, ans , cnt;
    cin >> n;
    ans = 1;
    cnt = 0;
    prev = -1;
    for(int i = 0 ; i < n ; i++){
        int tmp;
        cin >> tmp;
        if(prev < 0) prev = tmp;

        if(prev == tmp) cnt += 1;
        else{
            ans = max(ans, cnt);
            cnt = 1;
        }
        prev = tmp;
    }
    cout << ans;
    return 0;
}