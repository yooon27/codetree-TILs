#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n, x1,y1,x2,y2 , cnt;
    cnt = 0;
    cin >> n;
    int ans ;
    int arr[201][201];
    for(int i = 0; i < 201; i++){
        for(int j = 0; j< 201; j++) arr[i][j] = 0;
    }
    for(int i = 0; i < n; i++){
        cin >> x1 >> y1 >> x2 >> y2;
        x1 += 100;
        x2 += 100;
        y1 += 100;
        y2 += 100;
        for(int a = x1; a < x2 ; a++){
            for(int b = y1; b < y2; b++) arr[a][b] = 1;
        }
    }

    for(int i = 0; i < 201; i++){
        for(int j = 0; j< 201; j++){
            if(arr[i][j] == 1) cnt += 1;
         
        }
    }
    
    cout << cnt;
    return 0;
}