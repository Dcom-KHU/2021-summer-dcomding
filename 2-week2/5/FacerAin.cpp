/*
2주차 문제
방의 개수
직접 그려서 풀라는 문제는 아닌듯

사이클을 찾아보자.
그래프는 어떻게 만들 수 있을까?

사이클 탐색이야 DFS 한번으로 가능.

그래프는 어떻게 표현할 수 있을까?
*/

#include <iostream>
#include <vector>
#include <map>
#include <utility>
using namespace std;
//pair<y,x>
map<pair<pair<int,int>,pair<int,int>>,int> E;
map<pair<int,int>,int> V;

int dx[] = {0,1,1,1,0,-1,-1,-1};
int dy[] = {1,1,0,-1,-1,-1,0,1};

int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n;
	cin >> n;
	int cur_y = 0;
	int cur_x = 0;
	int next_y, next_x;
	int ans = 0;
	
	V.insert({{0,0}, 1});

	for(int i = 0; i < n; i++){
		int num;
		cin >> num;
		//대각선 교차하여 생기는 방 처리 => 2번씩 이동하자.
		for(int j =0; j < 2; j++){
			next_y = cur_y + dy[num];
		next_x = cur_x + dx[num];
		//방이 만들어지는 조건은?
		//이미 존재하는 정점을 새 경로(간선)으로 방문할 때
		if(V[{next_y,next_x}] == 1 && E[{{cur_y,cur_x}, {next_y,next_x}}] == 0){
			ans++;
		}
		V[{next_y,next_x}] = 1;
		E[{{cur_y,cur_x}, {next_y,next_x}}] = 1;
		E[{{next_y,next_x}, {cur_y,cur_x}}] = 1;
		cur_y = next_y;
		cur_x = next_x;
		}
	}
	
	cout << ans;
	return 0;
}