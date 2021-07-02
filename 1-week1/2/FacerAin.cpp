#include <iostream>
#include <cmath>
using namespace std;
/*
재귀버전 시간복잡도는? => O(2^n)
2^15은 약 3만 => 해결 가능
*/
int result = 0;
void hanoi(int src, int dst, int tmp, int num){
	
	if(num > 0){
		result+= dst;
		hanoi(src,tmp,dst,num-1);
		hanoi(tmp,dst,src,num-1);
	}

}

int main(){
	int n;
	cin >> n;
	hanoi(1,3,2,n);
	cout << result;
}