#include <iostream>
using namespace std;
#include <string>
#include <algorithm>
int main() {
    // 여기에 코드를 작성해주세요.
    string str1 , str2;
    cin >> str1;
    cin >> str2;
    sort(str1.begin(),str1.end());
    sort(str2.begin(),str2.end());
    if(str1 == str2) cout << "Yes";
    else cout << "No";
    return 0;
}