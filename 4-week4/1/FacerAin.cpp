#include <iostream>
#include <vector>

using namespace std;
/*
문제 조건대로 구현
vector erase 방식은 연산 효율이 좋지 않으나
문제의 크기가 작으므로 그냥 사용
*/

vector<int> moves;
vector<int> basket;
vector<vector<int>> board; 
int main(){
	int n , k;
	int ans = 0;
	cin >> n >> k;
	for(int i = 0; i < k; i++){
		int num;
		cin >> num;
		moves.push_back(num);
	}
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			if(i==0){
				vector<int> temp;
				board.push_back(temp);
			}
			int num;
			cin >> num;
			if(num != 0){
				board[j].push_back(num);

			}
		}
	}
	for(int i = 0; i < k; i++){
		int oper = moves[i] - 1;
		if(!board[oper].empty()){
			if(!basket.empty() && board[oper][0] == basket.back()){
				ans+= 2;
				basket.pop_back();
			}else{
				basket.push_back(board[oper][0]);

			}
			board[oper].erase(board[oper].begin());
		}
	}
	
	cout << ans;
}