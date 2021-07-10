#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>
/*
단순 DFS/BFS로는 풀 수 없다
백트래킹 사용할 것
간선의 개수(티켓의 수)와 노드의 수(동아리의 수)가 크지 않으므로 사용가능은 어림도 없지 ㅜn
정렬: nlgn + a(문자열 매칭)

map lg n
*/
using namespace std;
vector<vector<string>> ticket_v;
vector<vector<bool>> check_v;
vector<string> answer;
vector<int> idx_v;
int n;
map<string, int> m;
bool comp(string& v1, string& v2){
	if(v1.length() != v2.length()){
		return v1.length() < v2.length();
	}
	return v1 < v2;
}

bool DFS(string club, int visit_num){
	answer.push_back(club);
	//cout << club << endl;
	if(visit_num == n){
		return true;
	}
	int club_idx = m[club];
	//cout << club_idx << endl;
		for(int i = 0; i < ticket_v[club_idx].size(); i++){
		if(!check_v[club_idx][i]){
			check_v[club_idx][i] = true;
			if(DFS(ticket_v[club_idx][i], visit_num+1)){
				return true;
			}
			check_v[club_idx][i] = false;
		}
	}
	answer.pop_back();
	return false;
}

void DFS2(string club){
	idx_v.reserve(n+1);
	answer.push_back(club);
	//cout << club << endl
	int idx = -1;
	int club_idx = m[club];
	while(!answer.empty()){
		if(answer.size() == n+1){
			return;
		}
		
		club_idx = m[answer.back()];
		bool isExist = false;
		for(int i = idx+1; i < ticket_v[club_idx].size(); i++){
		if(!check_v[club_idx][i]){
			check_v[club_idx][i] = true;
			answer.push_back(ticket_v[club_idx][i]);
			//cout << answer.back() << endl;
			idx_v.push_back(i);
			isExist = true;
			break;
		}
			
	}
		if(!isExist){
				idx = idx_v.back();
				idx_v.pop_back();
				answer.pop_back();
				check_v[m[answer.back()]][idx] = false;
			}else{
			idx = -1;
		}
		
	//cout << club_idx << endl;
	}
}


int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int idx = 0;
	cin >> n;
	answer.reserve(n+1);
	for(int i = 0; i < n; i++){
		string s1, s2;
		cin >> s1 >> s2;
		vector<string> t_v;
		vector<bool> t_v2;
		if(m.find(s1) == m.end()){//키에 없을 때
			m.insert({s1, idx});
			idx++;
			ticket_v.push_back(t_v);
			check_v.push_back(t_v2);
		}

		if(m.find(s2) == m.end()){
			m.insert({s2, idx});
			//cout << s2 << idx << endl;
			idx++;
			ticket_v.push_back(t_v);
			check_v.push_back(t_v2);
		}
		ticket_v[m[s1]].push_back(s2);
		check_v[m[s1]].push_back(false);
		sort(ticket_v[m[s1]].begin(), ticket_v[m[s1]].end(),comp);
	}
	
	DFS2("DCOM");
	for(int i = 0; i < answer.size(); i++){
		cout << answer[i] << " ";
	}
	
	return 0;
	
}