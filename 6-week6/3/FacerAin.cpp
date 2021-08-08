#include <iostream>
using namespace std;

int n, m;
int map[505][505];
int dp[505][505];
int dy[] = {1,-1,0,0};
int dx[] = {0,0,1,-1};

bool isInside(int y, int x){
	return (y >= 0&& y < n) && ( x >=0 && x < m);
}

int DFS(int y, int x){
	if(y == n-1 && x == m-1){
		return 1;
	}
	if(dp[y][x] != -1){
		return dp[y][x];
	}
	dp[y][x] = 0;
	for(int i = 0; i < 4; i++){
		int next_y = y+dy[i];
		int next_x = x+dx[i];
		if(isInside(next_y,next_x) && map[next_y][next_x] < map[y][x]){
			dp[y][x] += DFS(next_y,next_x);
		}
	}
	return dp[y][x];
}

int main(){
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> n>> m;
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			cin >> map[i][j];
			dp[i][j] = -1;
		}
	}

	
	DFS(0,0);
	
	cout << dp[0][0];
	return 0;
}