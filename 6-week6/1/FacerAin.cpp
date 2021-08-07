/*
n이 홀수 일 때 (n+1)/2
1 2 3 4 5 6 7
2 4 6
4

1 2 3 4 5 6 7 8
2 4 6 8
4 8
8
n이 짝수 일때 n
*/

#include <iostream>
using namespace std;

int main(){
	int n;
	cin >> n;
	if(n%2==0){
		cout << n;
	}else{
		cout << (n+1)/2;
	}
	return 0;
	
}