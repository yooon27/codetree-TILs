#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n , cnt = 0;
    int arr[10001];
    cin >> n;
    for(int i = 0 ; i< n ; i ++){
        int tmp;
        cin >> tmp;
        arr[i] = tmp;
        cnt += tmp;
    }
    int ans = 0;
    for(int i = 0 ; i<n; i++){
        ans += abs((int)(cnt/n) - arr[i]);
    }
    cout << (int)(ans/2);
    return 0;
}