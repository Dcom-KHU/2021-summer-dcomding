#include <iostream>
using namespace std;

int main(){
	int n;
	cin >> n;
	long result = 1;
	while(result*2 <= n){
		result *= 2;
	}
	cout << result;
	return 0;
	
}