#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

int campus[11][11], n, m, dx[]={1,-1,0,0}, dy[]={0,0,1,-1}, bMinPos[7][2], bMaxPos[7][2], group[7], result;
stack<pair<int, int>> funcStack;
vector<pair<int, pair<int, int>>> bridges;

//2차원 배열의 유효한 위치인 지 확인하는 함수
bool canGotoPos(int x, int y){
	return 0<=x && x<n && 0<=y && y<m;
}

//union-find 함수
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
			if(campus[nCnt][mCnt] == -1) {
				++buildingCnt;
				bMinPos[buildingCnt][0] = bMinPos[buildingCnt][1] = 11;
				funcStack.push(make_pair(nCnt,mCnt));
				
				while(!funcStack.empty()){
					int x = funcStack.top().first, y = funcStack.top().second; funcStack.pop();
					campus[x][y] = buildingCnt;
					
					//아래 for문 탐색을 최소화 하기 위한 건물의 사각 영역 갱신
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
		for(int xCnt = bMinPos[bCnt][0]; xCnt<=bMaxPos[bCnt][0]; ++xCnt)
			for(int yCnt = bMinPos[bCnt][1]; yCnt<=bMaxPos[bCnt][1]; ++yCnt)
				
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
									//다음 지점이 자기 건물이 아니면서 거리가 1보다 크면 벡터에 저장
									else if(campus[nx][ny] != bCnt && val%10>1)
										bridges.push_back(make_pair(val%10, make_pair(min(bCnt, campus[nx][ny]), max(bCnt, campus[nx][ny]))));
										
								}
								//다음 다리 탐색을 위한 다리 기록 초기화
								campus[x][y] = 0;
							}
						}
					}
				}
	
	//unoin-find 초기 세팅
	for(int cnt=1; cnt<=6; ++cnt)
		group[cnt] = cnt;
	sort(bridges.begin(), bridges.end());
	bridges.erase(unique(bridges.begin(), bridges.end()),bridges.end());

	//최소 스패닝 트리를 이용한 간선 채택
	int matchCnt=1;
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