#include <iostream>
using namespace std;
#include <string>
#include <algorithm>
int main() {
    // 여기에 코드를 작성해주세요.
    int n, k ;
    string T;
    cin >> n >> k >> T;
    string arr[n];
    for(int i = 0 ; i<n ; i++) cin >> arr[i];
    sort(arr , arr+n);
    int check = 1;
    for(int i = 0 ; i<n ; i++){
        if(arr[i].substr(0,2) == T){
            if(check == k){
                cout << arr[i];
                break;
            }
            else if (check < k) check += 1;
            else break;
        }
    }
    return 0;
}