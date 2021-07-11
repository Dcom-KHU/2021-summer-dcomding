#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;

int n;
int item_cnt = 0;
int category_cnt;
vector<string> v;
int s_idx = 0;
int e_idx = 0;
map<string, int> m;
set<string> s;

void get_start_window(){
	int isFind = false;
	int idx = s_idx;
	while(!isFind){
		m[v[idx]] -= 1;
		if(m[v[idx]] == 0){
			item_cnt -= 1;
		}
		if(item_cnt != category_cnt){
			m[v[idx]] += 1;
			item_cnt += 1;
			s_idx = idx;
			isFind = true;
		}
		idx++;
	}
}

void get_end_window(){
	bool isFind = false;
	int idx = e_idx;
	while(!isFind){
		m[v[idx]] += 1;
		if(m[v[idx]] == 1){
			item_cnt += 1;
		}
		if(item_cnt == category_cnt){
			e_idx = idx;
			isFind = true;
		}
		idx++;
	}
}

int main(){

	int s_ans, e_ans, w_size;

	bool isBuy = false;
	cin >> n;
	for(int i = 0; i < n; i++){
		string s;
		cin >> s;
		v.push_back(s);
		m.insert({s,0});
		
	}
	
	category_cnt = m.size();
	//슬라이딩 윈도우의 끝 지점을 찾는다.
	get_end_window();
	
	//슬라이딩 윈도우의 시작 지점을 찾는다.
	get_start_window();
	
	s_ans = s_idx;
	e_ans = e_idx;
	w_size = e_idx - s_idx + 1;
	while(e_idx < n-1){
		e_idx++;
		m[v[e_idx]] += 1;
		
		if(m[v[e_idx]] == 1){
			item_cnt += 1;
		}
		

			get_start_window();
			if(w_size > e_idx - s_idx + 1){
					s_ans = s_idx;
					e_ans = e_idx;
			}
		
		
		
	}
	
	cout << s_ans + 1 << endl << e_ans + 1;
	
	
	
	
	return 0;
}