#include <iostream>
#include <vector>
#include <string>
/*
커서는 스택 2개로 간단하게 구현할 수 있다.
*/

using namespace std;

vector<char> v1;
vector<char> v2;
int main(){
	string s;
	cin >> s;
	for(int i = 0; i < s.size(); i++){
		char c = s[i];
		if(c == '<'){
			if(v1.empty()){
				continue;
			}else{
				v2.push_back(v1.back());
				v1.pop_back();
			}
		}
		else if(c == '>'){
			if(v2.empty()){
				continue;
			}else{
				v1.push_back(v2.back());
				v2.pop_back();
			}
		}
		else if(c == '-'){
			if(!v1.empty()){
				v1.pop_back();
			}else{
				continue;
			}
		}else{
			v1.push_back(c);
		}
	}
	
	for(int i = 0; i < v1.size(); i++){
		cout << v1[i];
	}
	for(int i =  v2.size() - 1; i >= 0; i--){
		cout << v2[i];
	}
	
	return 0;
	
}