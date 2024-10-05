#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    int number = 1;
    for(int i = 0 ; i<n; i++){
        for(int j = 0; j< n ; j++){
            cout << number << ' ';
            if(number == 9){
                number = 1;
            }
            else{
                number += 1;
            }

        }
        cout << endl;
    }
    return 0;
}