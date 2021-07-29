/*
시뮬레이션 문제
n의 크기가 10만이라 특별한 알고리즘 안써도 될듯
*/

#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

bool compare(pair<int,int> a, pair<int,int> b){
	if(a.first == b.first){
		return a.second < b.second;
	}
	return a.first < b.first;
}

vector<pair<int,int>> timetable;
vector<int> seats;
int ans[1005];

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

	for(int i = 0; i < n; i++){
		bool flag = false;
		//가능한 시간이 있는지 체크;
		for(int j = 0; j < seats.size(); j++){
			if(seats[j] <= timetable[i].first){
				flag = true;
				seats[j] = timetable[i].second;
				ans[j] += 1;
				break;
			}
		}
		
		if(!flag){
			seats.push_back(timetable[i].second);
			ans[seats.size() - 1] = 1;
		}
	}
	cout << seats.size() << endl;
	for(int i = 0; i < seats.size(); i++){
		cout << ans[i] << " ";
	}
	return 0;
}