/*
정답 화살표의 방향은 정해져있다.
구간의 개수가 적은 화살표의 방향이 답
...
*/

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
	string s;
	cin >> s;

	s += '2';//마지막 구간 처리를 위함
	int up_cnt = 0;
	int down_cnt = 0;
	
	for(int i = 0; i < s.size() - 1; i++){
		if(s[i] != s[i+1]){//구간의 끝일 때
			if(s[i] == '1'){
				up_cnt++;
			}else{
				down_cnt++;
			}
		}
	}
	cout << min(up_cnt,down_cnt);
	return 0;
}