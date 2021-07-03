#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
priority_queue<int,vector<int>,greater<int> > pq;

/*
stone이 2억, n이 20만이기 때문에 
단순 시뮬레이션으로는 풀 수 없다. 다른 방법을 생각해보자.

더 좋은 방법이 있을까?

ans를 어떻게 업데이트 할 것인가?
성공했다면 ans 갱신
아니라면 출력

*/
int n, k;
vector<int> stones;
int ans = 1;
int main(){
	cin >> n >> k;
	stones.resize(n);
	for(int i = 0; i < n; i++){
		cin >> stones[i];
		pq.push(stones[i]);
	}
	int ans = pq.top();
	int p_num = 0;
	for(int i = 0; i < n; i++){
		if(pq.top() == p_num){
			
			pq.pop();
			continue;
		}else{
			p_num = pq.top();
			pq.pop();
		}
		
		int temp = 0;
		for(int j = 0; j < n; j++){
			if(stones[j]  <= p_num){
				temp++;
				if(temp > k){
					cout << ans;
					return 0;
				}
			}else{
				temp = 0;
			}
		}
		
		ans = p_num;

	}
	cout << ans;
	return 0;
	
}

