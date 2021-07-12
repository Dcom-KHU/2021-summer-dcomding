#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int campus[11][11], n, m;
vector<pair<int, pair<int, int>>> bridges;

//2차원 배열의 유효한 위치인 지 확인하는 함수
bool canGotoPos(int x, int y){
	return 0<=x && x<n && 0<=y && y<m;
}

//dfs 건물, 다리 탐색용
int dx[]={1,-1,0,0}, dy[]={0,0,1,-1}, bCnt;
void dfs(int x, int y, int mode, int val){
	
	//건물 탐색용
	if(mode == -1){
		campus[x][y] = val;
		
		for(int cnt=0;cnt<4;++cnt){
			int nx = x+dx[cnt], ny = y+dy[cnt];
			if(canGotoPos(nx, ny) && campus[nx][ny] == -1)
				dfs(nx, ny, mode, val);
		}
	}
	
	//다리 탐색용
	else{
		int nx = x+dx[mode], ny = y+dy[mode];
		if(canGotoPos(nx, ny)){
			
			//다음 지점이 빈 공간이면 한칸 더감
			if(campus[nx][ny] == 0)
				dfs(nx, ny, mode, val+1);
			
			//다음 지점이 자기 건물이 아니면서 거리가 1보다 크면 벡터에 저장
			else if(campus[nx][ny] != bCnt && val>1)
				bridges.push_back(make_pair(val, make_pair(min(bCnt, campus[nx][ny]), max(bCnt, campus[nx][ny]))));
			
		}
	}
}

//union-find 함수
int group[7];
int findGroup(int bNum){
	if(bNum == group[bNum]) return bNum;
	return group[bNum] = findGroup(group[bNum]);
}

 
int main() {
	scanf("%d%d",&n,&m);
	for(int nCnt = 0; nCnt<n; ++nCnt)
		for(int mCnt = 0; mCnt<m; ++mCnt){
			scanf("%d",&campus[nCnt][mCnt]);
			//건물의 번호가 1번부터 시작하므로 존재여부와 건물번호에 차이를 두기 위해 존재여부는 -1로 저장함
			campus[nCnt][mCnt] = -campus[nCnt][mCnt];
		}
	
	//dfs를 통해 건물 특정짓기
	int buildingCnt = 0;
	for(int nCnt = 0; nCnt<n; ++nCnt)
		for(int mCnt = 0; mCnt<m; ++mCnt)
			
			//방문한 지점에 번호가 매겨지지 않은 건물이 있으면 건물에 번호를 붙여줌
			if(campus[nCnt][mCnt] == -1) 
				dfs(nCnt, mCnt, -1, ++buildingCnt);
			
	
	//dfs를 통해 각 건물을 연결하는 다리 만들기 bCnt는 dfs()에서도 사용됨
	for(bCnt = 1; bCnt<=buildingCnt; ++bCnt)
		for(int nCnt = 0; nCnt<n; ++nCnt)
			for(int mCnt = 0; mCnt<m; ++mCnt)
				
				//방문한 지점이 건물이면 한 방향으로 다리를 놓아봄
				if(campus[nCnt][mCnt] == bCnt)
					for(int cnt=0; cnt<4; ++cnt)
						dfs(nCnt, mCnt, cnt, 0);
				
	
	//unoin-find 초기 세팅
	for(int cnt=1; cnt<=6; ++cnt)
		group[cnt] = cnt;

	sort(bridges.begin(), bridges.end());
	bridges.erase(unique(bridges.begin(), bridges.end()),bridges.end());
	
	//최소 스패닝 트리를 이용한 간선 채택
	int matchCnt=1, result=0;
	for(int cnt=0; cnt<bridges.size(); ++cnt){
		int val = bridges[cnt].first, x = bridges[cnt].second.first, y = bridges[cnt].second.second;
		
		//채택된 두 건물이 서로 다른 그룹이면 다리를 선택함
		if(findGroup(x) != findGroup(y))
			group[findGroup(y)] = findGroup(x), ++matchCnt, result+=val;
		
		//모든 건물이 한 그룹으로 묶였으면 다리 선택을 그만둠.
		if(matchCnt == buildingCnt) break;
	}
	
	//모든 건물이 하나로 묶였으면 result, 아니면 불가능하다는 뜻이므로 -1을 출력
	printf("%d",matchCnt==buildingCnt?result:-1);

	return 0;
}