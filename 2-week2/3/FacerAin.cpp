#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
vector<vector<string>> v;
vector<string> q;
map<string, int> m;
int check[5005];
/*
자료형을 어떻게 구성할까?

*/
bool comp(string a, string b){
	if(a.length() != b.length()){
		return a.length() > b.length();
	}else{
		return a > b;
	}
}

void BFS(){
	
	q.push_back("DCOM");
	while(!q.empty()){
		string club = q.back();
		q.pop_back();
		int c_idx = m[club];
		check[c_idx] = 1;
		cout << club << " ";
		
		for(int i = 0; i < v[c_idx].size(); i++){
			string next_club = v[c_idx][i];
			v[c_idx][i] = "";
			if(next_club != ""){
				q.push_back(next_club);
			}
			

			
		}
		sort(q.begin(), q.end(), comp);
	}
	
}
int n;
int main(){
	cin >> n;
	int idx = 0;
	
	for(int i = 0; i < n; i++){
		string s1, s2;
		cin >> s1 >> s2;
		if(m.find(s1) != m.end()){//시작 정점이 있을때
			v[m[s1]].push_back(s2);
		}else{//시작 정점이 없을때
			m.insert({s1,idx});
			vector<string> temp_v;
			v.push_back(temp_v);
			v[idx].push_back(s2);
			idx++;
		}
		//끝 정점이 없을때
		if(m.find(s2) == m.end()){
			m.insert({s2,idx});
			vector<string> temp_v;
			v.push_back(temp_v);
			idx++;
		}
	}
	
	BFS();
	
	
	return 0;
}