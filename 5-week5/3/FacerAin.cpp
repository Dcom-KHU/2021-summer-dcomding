/*
시뮬레이션 문제
O(N^2)으로는 풀 수 없다
*/

#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <queue>

using namespace std;

priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>> > pq;

bool compare(pair<int,int> a, pair<int,int> b){
	if(a.first == b.first){
		return a.second < b.second;
	}
	return a.first < b.first;
}

vector<pair<int,int>> timetable;
vector<int> seats;
int ans[100005];

int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;
	for(int i = 0; i < n; i++){
		int start, end;
		cin >> start >> end;
		timetable.push_back({start, end});
	}
	
	sort(timetable.begin(), timetable.end(), compare);
	int seat_cnt = 0;
	for(int i = 0; i < n; i++){
		bool flag = false;
		//가능한 시간이 있는지 체크;
		if(!pq.empty() && pq.top().first <= timetable[i].first){
			ans[pq.top().second] += 1;
			pq.push({timetable[i].second, pq.top().second});
			pq.pop();
		}else{
			//cout << timetable[i].first << " " << timetable[i].second << endl;
			seat_cnt += 1;
			ans[seat_cnt-1] = 1;
			pq.push({timetable[i].second, seat_cnt - 1});
		}

	}
	cout << seat_cnt << endl;
	for(int i = 0; i < seat_cnt; i++){
		cout << ans[i] << " ";
	}
	return 0;
}