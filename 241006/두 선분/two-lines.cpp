#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int x1 , x2, x3, x4;
    cin >> x1 >> x2 >> x3 >> x4;
    if(x3 <= x2){
        cout <<"intersecting";
        exit(0);
    }
    if(x4 <= x1){
        cout <<"intersecting";
        exit(0);
    }
    cout << "nonintersecting";
    return 0;
}