#include <iostream>
#include <vector>
#include <map>
#define INF 999999999;
using namespace std;
/*
슬라이딩 윈도우 + 힙 구조
출처: https://sina-sina.tistory.com/39
*/
int n,k;
vector<int> stones;
int main(){
		cin >> n >> k;
	stones.resize(n);
	for(int i = 0; i < n; i++){
		cin >> stones[i];
	}
	
	multimap<int, int> m;
    multimap<int, int>::iterator iter;
	
	for(int i = 0; i < k; i++){
		m.insert({stones[i], -i});
	}
	
	int min = INF;
	iter = m.end();
	int max = (*--iter).first;
	if(min > max){
		min = max;
	}
	
	for(int i = k; i < stones.size(); i++){
		iter = m.find(stones[i-k]);
		m.erase(iter);
		m.insert({stones[i], -i});
		
		iter = m.end();
		max = (*--iter).first;
		if(min > max){
			min = max;
		}
		
	}
	cout << min;
}























/*
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
priority_queue<int,vector<int>,greater<int> > pq;


stone이 2억, n이 20만이기 때문에 
단순 시뮬레이션으로는 풀 수 없다. 다른 방법을 생각해보자.

더 좋은 방법이 있을까?



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
*/
