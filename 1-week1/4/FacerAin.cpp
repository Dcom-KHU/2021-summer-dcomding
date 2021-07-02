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

*/
int n, k;
vector<int> stones;
int main(){
	cin >> n >> k;
	stones.resize(n);
	for(int i = 0; i < n; i++){
		cin >> stones[i];
		pq.push(stones[i]);
	}
	int p_num = 0;
	int result = 0;
	for(int i = 0; i < n; i++){
		if(pq.top() == p_num){
			
			pq.pop();
			continue;
		}else{
			p_num = pq.top();
			pq.pop();
		}
		int tmp = 0;
		for(int j = 0; j < n; j++){
			if(stones[j]  <= p_num){
				tmp++;
				if(tmp > k){
					cout << p_num - 1;
					return 0;
				}
			}else{
				tmp = 0;
			}
		}

	}
	
}

