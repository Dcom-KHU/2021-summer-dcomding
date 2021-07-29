/*
브루트포스로 풀 경우
N^2 => 백만이므로 해결 가능
*/

#include <iostream>
#include <algorithm>
using namespace std;
int boxes[1005];
int map[1005];

int main(){
	int n;
	cin >> n;
	
	for(int i = 0; i < n; i++){
		cin >> boxes[i];
	}
	
	for(int i = 0; i <= n; i++){
		int idx = i-1;
		bool flag = false;
		int max_num = 0;
		while(idx >= 0){
			if(boxes[idx] < boxes[i]){
				max_num = max(max_num, map[idx]);
			}
			idx--;
		}
		map[i] = max_num + 1;
	}
	
	int result = 0;
	for(int i = 0; i < n; i++){
		result = max(result, map[i]);
	}
	
	cout << result;
	return 0;
}