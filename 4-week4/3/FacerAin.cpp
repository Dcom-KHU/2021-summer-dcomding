/*
단순한 BFS 문제
최단 거리 계산하는 BFS처럼 풀되 이동 조건에 회전만 추가하면 됨.

회전을 어떻게 구현할까?

*/
#include <iostream>
#include <queue>
#include <utility>
using namespace std;
int n;
int map[105][105];
int check[105][105][2];

int dy[] = {0,1,-1,0};
int dx[] = {1,0,0,-1};

int rdy1[] = {-1,-1,0,0};
int rdx1[] = {1,0,1,0};

int rdy2[] = {0,1,1,0};
int rdx2[] = {-1,0,-1,0};


bool isInside(int y, int x){
	return (y >= 0 && y < n) && (x >= 0 && x < n);
}

//구조체로 로봇을 표현하면 더 깔끔하게 구현할 수 있는데 귀찮아서 생략.
queue<pair<pair<int,int>,pair<int, int>>> q; //{{y,x},{direction,time}}
void BFS(){
	q.push({{0,0},{0,0}});
	while(!q.empty()){
		int cur_y = q.front().first.first;
		int cur_x = q.front().first.second;
		int dirt = q.front().second.first;
		int time = q.front().second.second;
		//cout << cur_y << " " << cur_x << " " << dirt << " " << time << "\n";
		q.pop();
			//탐색 종료 조건
		if((cur_y == n-1 && cur_x == n-2) || (cur_y == n-2 && cur_x == n-1)){
			cout << time;
			return;
		}
		
	

		for(int i = 0; i < 4; i++){//상하좌우 이동
			
			int next_y = cur_y + dy[i];
			int next_x = cur_x + dx[i];
			int next_y2 = next_y + dy[dirt];
			int next_x2 = next_x + dx[dirt];
			if(isInside(next_y,next_x) && isInside(next_y2, next_x2) && !check[next_y][next_x][dirt] && !map[next_y][next_x] && !map[next_y2][next_x2]){
				q.push({{next_y,next_x}, {dirt,time+1}});
				check[next_y][next_x][dirt] = 1;
			}
		}
		
		
		for(int i = 0; i < 4; i++){
			int next_y, next_x, check_y, check_x;
			if(!dirt){//가로
				next_y = cur_y + rdy1[i];
				next_x = cur_x + rdx1[i];
				check_y = next_y;
				check_x = cur_x  + ((rdx1[i] + 1)%2);
			}else{//세로
				next_y = cur_y + rdx2[i];
				next_x = cur_x + rdy2[i];
				check_y = cur_y + ((rdy2[i] + 1)%2);
				check_x = next_x;
			}
			
			if(isInside(next_y,next_x) && isInside(check_y,check_x) && !check[next_y][next_x][(dirt+1)%2] && !map[next_y][next_x] && !map[check_y][check_x]){
				q.push({{next_y,next_x}, {(dirt+1)%2, time + 1}});
				check[next_y][next_x][(dirt+1)%2] = 1;
			}
			

		}
		
	}
}

int main(){
	cin >> n;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			cin >> map[i][j];
		}
	}
	
	BFS();

	
	
	return 0;
}
