//0주차 1번 구구단
#include <iostream>
using namespace std;
int n;
int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	for(int i = 1; i <=n; i++){
		cout << n << " * " << i << " = " << n*i << '\n';
	}
	return 0;
}