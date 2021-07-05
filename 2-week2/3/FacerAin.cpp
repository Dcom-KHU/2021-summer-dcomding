#include <iostream>
#include <vector>
#include <algorithm>
/*
단순 DFS/BFS로는 풀 수 없다
백트래킹 사용할 것
간선의 개수(티켓의 수)와 노드의 수(동아리의 수)가 크지 않으므로 사용가능

*/
using namespace std;
vector<vector<string>> ticket_v;
vector<string> answer;
int check[100005];
int n;
bool comp(const vector<string>& v1, const vector<string>& v2){
	if(v1[1].length() != v2[1].length()){
		return v1[1].length() < v2[1].length();
	}
	return v1[1] < v2[1];
}

bool DFS(string club, int visit_num){
	answer.push_back(club);
	if(visit_num == n){
		return true;
	}
	for(int i = 0; i < ticket_v.size(); i++){
		if(ticket_v[i][0] == club && !check[i]){
			check[i] = 1;
			if(DFS(ticket_v[i][1], visit_num+1)){
				return true;
			}
			check[i] = 0;
		}
	}
	answer.pop_back();
	return false;
}

int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n;
	ticket_v.resize(n);
	answer.reserve(n);
	for(int i = 0; i < n; i++){
		string s1, s2;
		cin >> s1 >> s2;
		vector<string> temp_v(2);
		temp_v[0] = s1;
		temp_v[1] = s2;
		ticket_v[i] = temp_v;
	}
	sort(ticket_v.begin(),ticket_v.end(),comp);
	
	DFS("DCOM",0);
	for(int i = 0; i < answer.size(); i++){
		cout << answer[i] << " ";
	}
	return 0;
	
}