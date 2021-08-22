/*
유사 회문을 검출하는 방법은?


*/

#include <iostream>
#include <string>
#include <string>

using namespace std;
int main(){
	string word;
	cin >> word;
	int L_idx = 0;
	int R_idx = word.size()-1;
	int flag = 0;
	for(int i = 0; i < word.size()/2; i++){
		if(word[L_idx] == word[R_idx]){
			L_idx++;
			R_idx--;
		}else if(word[L_idx+1] == word[R_idx] && flag == 0){
			flag++;
			word.erase(L_idx, L_idx+1);
			R_idx--;
		}else if(word[L_idx] == word[R_idx-1] && flag == 0){
			flag++;
			word.erase(R_idx, R_idx+1);
			R_idx--;
		}else{
			flag = 2;
			break;
		}
	}
	
	cout << flag;
	
	return 0;
}