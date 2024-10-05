#include <iostream>
using namespace std;
#include <algorithm>

int main() {
    // 여기에 코드를 작성해주세요.
    int n , flag;
    cin >> n;
    int arr1[n] , arr2[n];
    for(int i; i < n ; i++)cin >> arr1[i];
    for(int i; i< n ; i++) cin >> arr2[i];
    sort(arr1, arr1+n);
    sort(arr2, arr2+n);
    flag = 0;
    for(int i; i<n; i++){
        if(arr1[i] == arr2[i]) continue;
        flag = 1;
    }
    if(flag == 0) cout << "Yes";
    else cout << "No";
    
    return 0;
}