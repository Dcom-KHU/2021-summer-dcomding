/*
모든 경우의 수를 탐색?
N^2이므로 10000000000 백억이므로 해결 불가

분할 정복 활용을 활용하자!
사각형이 왼쪽, 오른쪽, 걸쳐있을 케이스 고려
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N;
vector<int> heights;

//left ~ right까지 찾을 수 있는 사각형 중 가장 큰 사각형 반환
int search(int left, int right){
	if(left == right){//base
		return heights[left];
	}
	int mid = (left + right) / 2;
	//왼쪽, 오른쪽
	int ret = max(search(left, mid), search(mid+1, right));
	
	
	//걸쳐있을 케이스
	int height = min(heights[mid], heights[mid+1]);
	ret = max(ret, height * 2);
	int l_idx = mid;
	int r_idx = mid + 1;
	while(left < l_idx || r_idx < right){
		if(r_idx < right && (l_idx == left || heights[l_idx - 1] < heights[r_idx + 1])){
			r_idx++;
			height = min(height, heights[r_idx]);
		}else{
			l_idx--;
			height = min(height, heights[l_idx]);
		}
		
		ret = max(ret, height * (r_idx - l_idx + 1));
	}
	return ret;
}

int main(){
	cin >> N;
	heights.resize(N);
	for(int i = 0; i < N; i++){
		cin >> heights[i];
	}
	cout << search(0 , N-1);
	return 0;
}