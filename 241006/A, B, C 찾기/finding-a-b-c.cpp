#include <iostream>
using namespace std;
#include <algorithm>
int main() {
    // 여기에 코드를 작성해주세요.
    int arr[7];
    for(int i = 0 ; i < 7; i++) cin >> arr[i];
    sort(arr, arr+7);
    int check = (arr[6] * 2);
    check -= arr[5];
    check -= arr[4];
    for(int i = 0 ; i<4; i++){
        if(arr[i] == check) continue;
        cout << arr[i] << ' ';
    }
    return 0;
}