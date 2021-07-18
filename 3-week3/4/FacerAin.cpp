#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>
using namespace std;
const int MAX = 105;
int N, M;
int map[MAX][MAX];
int visit[MAX][MAX];
int dy[] = {1,-1,0,0};
int dx[] = {0,0,1,-1};
vector<pair<pair<int,int>,int>> bridge; //{src,dst,len}

struct DisjointSet {
	vector<int> parent;
	DisjointSet(int n): parent(n) {
		for(int i = 1; i <= n; i++){
			parent[i] = i;
		}
	}
	int find(int u) const {
		if(u==parent[u]){
			return u;
		}
		return find(parent[u]);
	}
	void merge(int u, int v){
		u = find(u);
		v = find(v);
		if(u == v) return;
		parent[u] = v;
	}
};

bool compare(pair<pair<int,int>,int> a, pair<pair<int,int>,int> b){
	return a.second < b.second;
}

bool isInside(int y, int x){
	return (y >= 0 && y < N) && (x>= 0 &&  x < M);
}

void make_island(int y, int x, int label){
	queue<pair<int,int>> q;
	q.push({y,x});
	while(!q.empty()){
		int cur_y = q.front().first;
		int cur_x = q.front().second;
		map[cur_y][cur_x] = label;
		visit[cur_y][cur_x] = 1;
		q.pop();
		for(int i = 0; i < 4; i++){
			int next_y = cur_y + dy[i];
			int next_x = cur_x + dx[i];
			if(isInside(next_y, next_x) && !visit[next_y][next_x] && map[next_y][next_x]){
				q.push({next_y,next_x});
			}
		}
	}
	return;
}

void make_bridge(int y, int x, int label){
	for(int i = 0; i < 4; i++){
		int next_y = y+dy[i];
		int next_x = x+dx[i];
		int len = 0;
		if(isInside(next_y,next_x) && !map[next_y][next_x]){
			while(1){
				if(!isInside(next_y,next_x) || map[next_y][next_x] == label){
					break;
				}
				
				if(!map[next_y][next_x]){
					len++;
				}else{
					if(len > 1){//다리의 길이는 2 이상이어야 하므로
						bridge.push_back({{label, map[next_y][next_x]}, len});
						break;
					}
					break;
				}
				next_y += dy[i];
				next_x += dx[i];
			
		}
		}
	}
}

int main(){
	cin >> N >> M;
	int ans = 0;
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			cin >> map[i][j]; 
		}
	}
	int cnt = 0;
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			if(map[i][j] && !visit[i][j]){
				cnt++;
				make_island(i,j,cnt);
			}
		}
	}
	
	
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			if(map[i][j]){
				make_bridge(i,j,map[i][j]);
			}
		}
	}
	sort(bridge.begin(), bridge.end(), compare);
	DisjointSet sets(cnt);
	for(int i = 0; i < bridge.size(); i++){
		int src = bridge[i].first.first;
		int dst = bridge[i].first.second;
		if(sets.find(src) != sets.find(dst)){
			ans += bridge[i].second;
			sets.merge(src, dst);
		}
	}
	
	int check_node = sets.find(1);
	for(int i = 2; i <= cnt; i++){
		if(check_node != sets.find(i)){
			ans = -1;
			break;
		}
	}
	
	cout << ans;
	
	
	
	return 0;
}