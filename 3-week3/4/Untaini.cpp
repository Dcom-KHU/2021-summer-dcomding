#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
#include <queue>
using namespace std;

#define pii pair<int, int>

int campus[11][11], n, m, dx[]={1,-1,0,0}, dy[]={0,0,1,-1}, bMinPos[7][2], bMaxPos[7][2], group[10], result;
stack<pii> funcStack;
priority_queue<pair<int, pii>, vector<pair<int, pii>>, greater<pair<int, pii>>> pq;

bool canGotoPos(int x, int y){
	return 0<=x && x<n && 0<=y && y<m;
}

int findGroup(int bNum){
	if(bNum == group[bNum]) return bNum;
	return group[bNum] = findGroup(group[bNum]);
}
 
int main() {
	scanf("%d%d",&n,&m);
	//입력 받기
	for(int nCnt = 0; nCnt<n; ++nCnt)
		for(int mCnt = 0; mCnt<m; ++mCnt){
			scanf("%d",&campus[nCnt][mCnt]);
			campus[nCnt][mCnt] = -campus[nCnt][mCnt];
		}
	
	//dfs를 통해 건물 특정짓기
	int buildingCnt = 0;
	for(int nCnt = 0; nCnt<n; ++nCnt)
		for(int mCnt = 0; mCnt<m; ++mCnt)
			if(campus[nCnt][mCnt] == -1) {
				++buildingCnt;
				bMinPos[buildingCnt][0] = bMinPos[buildingCnt][1] = 11;
				funcStack.push(make_pair(nCnt,mCnt));
				
				while(!funcStack.empty()){
					int x = funcStack.top().first, y = funcStack.top().second; funcStack.pop();
					campus[x][y] = buildingCnt;
					
					bMinPos[buildingCnt][0] = min(x, bMinPos[buildingCnt][0]);
					bMinPos[buildingCnt][1] = min(y, bMinPos[buildingCnt][1]);
					bMaxPos[buildingCnt][0] = max(x, bMaxPos[buildingCnt][0]);
					bMaxPos[buildingCnt][1] = max(y, bMaxPos[buildingCnt][1]);
					
					for(int cnt=0;cnt<4;++cnt){
						int nx = x+dx[cnt], ny = y+dy[cnt];
						if(canGotoPos(nx, ny) && campus[nx][ny] == -1)
							funcStack.push(make_pair(nx,ny));
					}
				}
			}
	
	//dfs를 통해 각 건물을 연결하는 다리 만들기 (10: 오른쪽, 20: 왼쪽, 30: 아래, 40: 위 / 일의자리 숫자가 거리)
	for(int bCnt = 1; bCnt<=buildingCnt; ++bCnt)
		
		//xCnt, yCnt는 for문을 최대한 적게 돌기 위한 처리
		for(int xCnt = 0; xCnt<n; ++xCnt)
			for(int yCnt = 0; yCnt<m; ++yCnt)
				
				//방문한 지점이 건물이면
				if(campus[xCnt][yCnt] == bCnt){
					for(int cnt=0; cnt<4; ++cnt){
						int tx = xCnt+dx[cnt], ty = yCnt+dy[cnt];
						
						//다음 지점이 빈 공간인 것 확인하기
						if(canGotoPos(tx, ty) && campus[tx][ty] == 0){
							campus[tx][ty] = cnt*10+11;
							funcStack.push(make_pair(tx, ty));
							
							//한 방향으로 끝까지 가기 위한 스택
							while(!funcStack.empty()){
								int x = funcStack.top().first, y = funcStack.top().second, val = campus[x][y]; funcStack.pop();
								int nx = x+dx[val/10-1], ny = y+dy[val/10-1];
								if(canGotoPos(nx, ny)){
									//다음 지점이 빈 공간이면 한칸 더감
									if(campus[nx][ny] == 0){
										funcStack.push(make_pair(nx, ny));
										campus[nx][ny] = val+1;
									}
									//다음 지점이 자기 건물이 아니면서 거리가 1보다 크면 우선순위 큐에 저장
									else if(campus[nx][ny] != bCnt && val%10>1)
										pq.push(make_pair(val%10, make_pair(min(bCnt, campus[nx][ny]), max(bCnt, campus[nx][ny]))));
										
								}
								//다리 기록 초기화
								campus[x][y] = 0;
							}
						}
					}
				}
	
	//unoin-find 초기 세팅
	for(int cnt=1; cnt<=6; ++cnt)
		group[cnt] = cnt;
	
	//최소 스패닝 트리를 이용한 간선 채택
	int matchCnt=1;
	while(!pq.empty()){
		pair<int, pii> edge = pq.top(); pq.pop();
		int val = edge.first, x = edge.second.first, y = edge.second.second;
		if(findGroup(x) != findGroup(y)){
			group[findGroup(y)] = findGroup(x), ++matchCnt, result+=val;
			//printf("(%d %d %d), ",x,y,val);
		}
		if(matchCnt == buildingCnt) break;
	}
	
	printf("%d",matchCnt==buildingCnt?result:-1);

	return 0;
}