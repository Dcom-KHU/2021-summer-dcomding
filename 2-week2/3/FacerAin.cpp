#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
/*
단순 DFS/BFS로는 풀 수 없다
백트래킹 사용할 것
간선의 개수(티켓의 수)와 노드의 수(동아리의 수)가 크지 않으므로 사용가능은 어림도 없지
정렬: nlgn + a(문자열 매칭)
백트래킹: n!....?

map lg n
*/
using namespace std;
vector<vector<string>> ticket_v;
vector<vector<int>> check_v;
vector<string> answer;
int check[100005];
int n;
map<string, int> m;
bool comp(string v1, string v2){
	if(v1.length() != v2.length()){
		return v1.length() < v2.length();
	}
	return v1 < v2;
}

bool DFS(string club, int visit_num){
	answer.push_back(club);
	if(visit_num == n){
		return true;
	}
	int club_idx = m[club];
		for(int i = 0; i < ticket_v[club_idx].size(); i++){
		if(!check_v[club_idx][i]){
			check_v[club_idx][i] = 1;
			if(DFS(ticket_v[club_idx][i], visit_num+1)){
				return true;
			}
			check_v[club_idx][i] = 0;
		}
	}
	/*
	//아래 반복문을 더욱 개선할 수 있는 방법은?
	for(int i = 0; i < ticket_v.size(); i++){
		if(!check[i] && ticket_v[i][0] == club){
			check[i] = 1;
			if(DFS(ticket_v[i][1], visit_num+1)){
				return true;
			}
			check[i] = 0;
		}
	}
	*/
	answer.pop_back();
	return false;
}

int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int idx = 0;
	cin >> n;
	ticket_v.resize(n);
	answer.reserve(n);
	for(int i = 0; i < n; i++){
		string s1, s2;
		cin >> s1 >> s2;
		vector<string> t_v;
		vector<int> t_v2;
		if(m.find(s1) == m.end()){//키에 없을 때
			m.insert({s1, idx});
			idx++;
			ticket_v.push_back(t_v);
			check_v.push_back(t_v2);
		}
		ticket_v[m[s1]].push_back(s2);
		check_v[m[s1]].push_back(0);
		if(m.find(s2) != m.end()){
			m.insert({s2, idx});
			idx++;
			ticket_v.push_back(t_v);
			check_v.push_back(t_v2);
		}
	}
	for(int i = 0; i < ticket_v.size(); i++){
		sort(ticket_v[i].begin(), ticket_v[i].end(),comp);
	}
	
	DFS("DCOM",0);
	for(int i = 0; i < answer.size(); i++){
		cout << answer[i] << " ";
	}
	return 0;
	
}