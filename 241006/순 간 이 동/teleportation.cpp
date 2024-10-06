#include <iostream>
using namespace std;
#include <stdlib.h>
#include <algorithm>
int main() {
    // 여기에 코드를 작성해주세요.
    int a, b, x, y ;
    cin >> a >> b >> x >> y;
    int ans;
    ans = abs(a-b);
    int tmp;
    tmp = min(abs(a-x) + abs(b-y) , abs(b-x) + abs(a-y));
    ans = min(ans, tmp);
    cout << ans;
    return 0;
}