#include <iostream>
#include <vector>
using namespace std;
string s;
/*
1000 * 1000 = 백만
완전 탐색으로 해결가능
*/
int s_idx, e_idx;
void move_idx(int& idx){
	idx++;
	if(idx >= s.size()){
		idx = 0;
		return;
	}
	return;
}

bool check_pair(char s1, char s2){
	if(s1 == '(' && s2 == ')'){
		return true;
	}
	if(s1 == '{' && s2 == '}'){
		return true;
	}
	if(s1 == '[' && s2 == ']'){
		return true;
	}
	return false;
}
bool check(){
	vector<char> v;
	int cur_idx = s_idx;
	while(cur_idx != e_idx){
		if(s[cur_idx] == '{' || s[cur_idx] == '('|| s[cur_idx] == '['){//여는 괄호일 때
			v.push_back(s[cur_idx]);
		}
		else{//닫는 괄호일 때
			if(!v.empty() && check_pair(v.back(), s[cur_idx])){
				v.pop_back();
			}else{
				return false;
			}
		}
		move_idx(cur_idx);
		
	}
	
	//마지막 idx 처리
	if(!v.empty()){
		if(check_pair(v.back(), s[cur_idx])){
			v.pop_back();
		}
		if(!v.empty()){
			return false;
		}
		return true;
		
	}else{
		return false;
	}

}
int main(){
	cin >> s;
	s_idx = 0;
	e_idx = s.size() - 1;
	int ans = 0;
	for(int i = 0; i < s.size(); i++){
		if(check()){
			ans++;
		}
		move_idx(s_idx);
		move_idx(e_idx);
	}
	cout << ans;
	return 0;
}