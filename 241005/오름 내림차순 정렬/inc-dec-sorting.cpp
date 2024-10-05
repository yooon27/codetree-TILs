#include <iostream>
using namespace std;
#include <algorithm>
#include <functional>

int main() {
    // 여기에 코드를 작성해주세요.
    int n ;
    cin >> n;
    int arr[n];
    for(int i = 0; i<n ; i++) cin >> arr[i];

    sort(arr, arr+n);
    for(int i = 0; i<n; i++) cout << arr[i] << ' ';
    cout << endl;
    for(int j = n-1 ; j >= 0 ;j--) cout << arr[j] << ' ';

    return 0;
}