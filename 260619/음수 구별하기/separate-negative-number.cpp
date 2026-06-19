#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    if(n >= 0){
        cout << n << endl;
    }else if(n < 0){
        cout << n << "\nminus" << endl;
    }
    return 0;
}