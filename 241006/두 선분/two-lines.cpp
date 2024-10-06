#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int x1 , x2, x3, x4;
    cin >> x1 >> x2 >> x3 >> x4;
    int arr[102];
    for(int i = 0 ; i<101 ; i++) arr[i] = 0;
    for(int i = x1 ; i<x2 ; i++) arr[i] += 1;
    for(int i = x3 ; i <x4; i++) arr[i] += 1;
    for(int i = 0; i < 101; i ++ ){
        if(arr[i] > 1){
            cout << "intersecting";
            exit(0);
        }

    }
    cout << "nonintersecting";
    
    return 0;
}