#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

/*
시간 복잡도 O(nlgn)
n은 100,000이므로 해결 가능.

sum의 최대 크기 => 100,000 * 10,000 => int 형으로 표현 가능

*/
int main(){
	int n, k;
	cin >> n >> k;
	vector<int> num_v(n);
	for(int i = 0; i < n; i++){
		cin >> num_v[i];
	}
	sort(num_v.begin(), num_v.end());
	
	int start_idx = (k+1)/2;
	int end_idx = n - k/2;
	
	int sum = 0;
	for(int i = start_idx; i< end_idx; i++){
		sum += num_v[i];
	}
	
	cout << sum;
	return 0;
}