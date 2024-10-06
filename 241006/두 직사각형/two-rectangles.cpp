#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int x1 , y1 , x2, y2 , a1, a2, b1,b2;

    cin >> x1 >> y1 >> x2 >> y2;
    cin >> a1 >> b1 >> a2 >> b2;
    int arr[101][101];
    for(int i = 0 ; i < 100 ; i++){
        for(int j = 0 ; j < 100 ; j++) arr[i][j] = 0;
    }

    for(int i = x1 ; i <= x2; i++){
        for(int j = y1; j < y2; j++) arr[i][j] += 1;
    }
    for(int i = a1 ; i <= a2 ; i++){
        for(int j = b1 ; j <= b2 ; j++) arr[i][j] += 1;
    }

    for(int i = 0; i < 100 ; i++){
        for(int j = 0; j < 100; j++){
            if(arr[i][j] > 1){
                cout << "overlapping";
                exit(0);
            }
        }
    }
    cout << "nonoverlapping";

    return 0;
}