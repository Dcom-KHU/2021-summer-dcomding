#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;

#define pii pair<int, int>

int n, board[102][102], temp, robotBoard[102][102][2], dx[]={1,-1,0,0}, dy[]={0,0,1,-1};
queue<pair<pii, pii>> bfsQueue;

int main()
{
    scanf("%d",&n);
    for(int row=1; row<=n; ++row)
        for(int col=1; col<=n; ++col){
            scanf("%d",&temp);
            //board에서 0을 장애물로 이용하기 위해 입력받은 값에서 0->1, 1->0으로 바꿔서 저장함
            //이후로 1이 빈칸, 0이 장애물이 됨
            //이 방법을 쓰면 저장되지 않은 board의 모든 칸이 장애물로 인식되어 따로 벽 처리해주지 않아도 됨
            board[row][col] = !temp;
        }
    
    //robotBoard는 모두 0으로 초기화되어 있기 때문에 초기값과 방문값에 차이를 두기 위해 첫 좌표를 1로 설정함
    //앞으로 0이면 방문하지 않은 좌표, 0이 아니면 방문했던 좌표가 됨
    robotBoard[1][1][0] = 1;
    bfsQueue.push(make_pair(make_pair(1,1),make_pair(1,2)));
    
    //로봇의 왼쪽/위쪽 팔이 있는 좌표가 값을 저장할 좌표가 됨
    //따라서 bfsQueue에 새로운 좌표를 넣을 때는 항상 first가 왼쪽/위쪽 팔의 좌표가 되도록 넣어야 함
    while(!bfsQueue.empty()){
        //mode는 0일 때 가로, 1일 때 세로를 뜻함. lu = left/up, rd = right/down, n = next를 뜻함
        pii luPos = bfsQueue.front().first, rdPos = bfsQueue.front().second;
        int lux = luPos.first, luy = luPos.second, rdx = rdPos.first, rdy = rdPos.second,
            mode = luy == rdy, val = robotBoard[lux][luy][mode]+1;
        bfsQueue.pop();
        
        //cnt 0:아래쪽이동, 1:위쪽이동, 2:오른쪽이동, 3:왼쪽이동
        for(int cnt=0; cnt<4; ++cnt){
            int lunx = lux + dx[cnt], luny = luy + dy[cnt],
                rdnx = rdx + dx[cnt], rdny = rdy + dy[cnt];
            pii lunPos = make_pair(lunx,luny), rdnPos = make_pair(rdnx,rdny);
            
            //로봇이 이동할 좌표가 모두 빈칸(=1)이라면
            if(board[lunx][luny] && board[rdnx][rdny]){
                
                //상하좌우용 코드
                //다음 좌표를 방문하지 않았다면 방문값을 저장하고 bfsQueue에 넣음
                if(!robotBoard[lunx][luny][mode]){
                    robotBoard[lunx][luny][mode] = val;
                    bfsQueue.push(make_pair(lunPos,rdnPos));
                }
            
                //회전용 코드
                //로봇이 가로모드일 때 상/하로 이동할 수 있으면 좌상,우상/좌하,우하로 회전할 수 있음
                //로봇이 세로모드일 때 좌/우로 이동할 수 있으면 좌상,좌하/우상,우하로 회전할 수 있음
                //cnt<=1 : 상하이동, cnt>1 : 좌우이동, !mode : 세로모드, mode : 가로모드
                if(cnt/2 == mode){ // == (cnt>1 && mode) || (cnt<=1 && !mode)
                    if(cnt%2){ //(cnt, mode) : (1,0), (3,1)
                        
                        //로봇이 위쪽/왼쪽으로 이동했을 때는 원래 좌표보다 이동한 좌표가 더 작기 때문에 이동한 좌표를 기준으로 방문 여부를 확인함
                        if(!robotBoard[lunx][luny][!mode]){
                            robotBoard[lunx][luny][!mode] = val;
                            bfsQueue.push(make_pair(lunPos, luPos));
                        }
                        if(!robotBoard[rdnx][rdny][!mode]){
                            robotBoard[rdnx][rdny][!mode] = val;
                            bfsQueue.push(make_pair(rdnPos, rdPos));
                        }
                    }
                    else{ //(cnt,mode) : (0,0), (2,1)
            
                        //로봇이 아래쪽/오른쪽으로 이동했을 때는 원래 좌표가 이동한 좌표보다 더 작기 때문에 원래 좌표를 기준으로 방문 여부를 확인함
                        if(!robotBoard[lux][luy][!mode]){
                            robotBoard[lux][luy][!mode] = val;
                            bfsQueue.push(make_pair(luPos, lunPos));
                        }
                        if(!robotBoard[rdx][rdy][!mode]){
                            robotBoard[rdx][rdy][!mode] = val;
                            bfsQueue.push(make_pair(rdPos, rdnPos));
                        }
                    }
                    //if-else 없이 min,max 처리하면 코드 수가 줄어들지만, 보기 힘들까봐 min,max처리는 하지 않음
                }
            }
        }
    }
    
    //(n,n)에 로봇이 걸치는 가로 좌표(n,n-1), 세로 좌표(n-1,n) 중 더 작은 값을 출력함
    //0이면 10억을 반환해서 선택되지 않도록 하고 로봇의 시작점을 1로 잡았으니 1을 빼줌
    printf("%d",min(robotBoard[n][n-1][0]?robotBoard[n][n-1][0]:1<<30,robotBoard[n-1][n][1]?robotBoard[n-1][n][1]:1<<30)-1);
        
    return 0;
}
