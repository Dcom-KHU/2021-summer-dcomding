#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>
#include <queue>
/*
단순 DFS/BFS로는 풀 수 없다
백트래킹 사용할 것
가지치기 할 수 있는 방법은?
어차피 모든 간선을 방문해야한다. -> 오일러 서킷
간선의 개수(티켓의 수)와 노드의 수(동아리의 수)가 크지 않으므로 사용가능은 어림도 없지 ㅜn
정렬: nlgn + a(문자열 매칭)
매번 정렬하는 것도 부하가 심하다.
priority_queue 사용할 것


map lg n
*/
using namespace std;

struct compare{
	bool operator() (const string& s1, const string& s2){
	if(s1.length() != s2.length()){
		return s1.length() > s2.length();
	}
	return s1 > s2;
	}
};



vector<priority_queue<string, vector<string>, compare>> ticket_pv;
vector<string> answer;
vector<string> check_s;
int n;
map<string, int> m;
int c_num;



/*
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
*/

/*
굳이 체크를 할 이유가 없다.
바로 스택으로 구현 가능
오일러 회로 한붓그리기 문제 변형으로 생각하자.
*/
void DFS2(string club){
	check_s.push_back(club);
	while(c_num >= 0){
		string cur_club = check_s.back();
		int cur_club_idx = m[cur_club];
		if(!ticket_pv[cur_club_idx].empty()){
			check_s.push_back(ticket_pv[cur_club_idx].top());
			ticket_pv[cur_club_idx].pop();
		}else{
			answer.push_back(check_s.back());
			check_s.pop_back();
			c_num--;
		}
			
		
	//cout << club_idx << endl;
	}
}


int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int idx = 0;
	cin >> n;
	c_num = n;
	answer.reserve(n+1);
	for(int i = 0; i < n; i++){
		string s1, s2;
		cin >> s1 >> s2;
		priority_queue<string, vector<string>, compare> pq;
		if(m.find(s1) == m.end()){//키에 없을 때
			m.insert({s1, idx});
			idx++;
			ticket_pv.push_back(pq);
		}

		if(m.find(s2) == m.end()){
			m.insert({s2, idx});
			idx++;
			ticket_pv.push_back(pq);
		}
		int v_idx = m[s1];
		ticket_pv[v_idx].push(s2);
	}
	
	DFS2("DCOM");
	for(int i =  answer.size() - 1; i >= 0; i--){
		cout << answer[i] << " ";
	}
	
	return 0;
	
}