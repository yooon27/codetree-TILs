#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n , m , ans;
    cin >> n >> m;
    int arr[n];
    ans = 0;
    for(int i = 0 ; i< n ; i++){
        cin >> arr[i];
    }
    for(int i = 0 ; i<n ; i++){
        if(arr[i] == 1){
            if(i + (2*m) > n-1){
                for(int k = i ; k < n ; k++) arr[k] = 0;
            }
            else{
                for(int k = i ; k <= i + (2*m) ; k++) arr[k] = 0;
            }

            ans++;

        }
    }
    cout << ans;

    return 0;
}