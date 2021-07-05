#include <iostream>
#include <vector>
#include <algorithm>
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
}

int main(){
	cin >> n;
	for(int i = 0; i < n; i++){
		string s1, s2;
		cin >> s1 >> s2;
		vector<string> temp_v(2);
		temp_v[0] = s1;
		temp_v[1] = s2;
		ticket_v.push_back(temp_v);
	}
	sort(ticket_v.begin(),ticket_v.end(),comp);
	
	DFS("DCOM",0);
	for(int i = 0; i < answer.size(); i++){
		cout << answer[i] << " ";
	}
	return 0;
	
}