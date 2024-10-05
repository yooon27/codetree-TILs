#include <iostream>
using namespace std;
#include <algorithm>
int main() {
    // 여기에 코드를 작성해주세요.
    int n, arr[2002];
    cin >> n;
    for(int i = 0 ; i<n*2 ; i++){
        cin >> arr[i];
    }
    sort(arr, arr+2*n);
    int ans = 0;
    for(int i = 0; i < n ; i++) ans = max(ans,arr[i] + arr[2*n - 1 - i]);
    cout << ans;
    return 0;
}