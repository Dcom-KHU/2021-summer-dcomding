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
            board[row][col] = !temp;
        }
    
    robotBoard[1][1][0] = 1;
    bfsQueue.push(make_pair(make_pair(1,1),make_pair(1,2)));
    
    while(!bfsQueue.empty()){
        pii luPos = bfsQueue.front().first, rdPos = bfsQueue.front().second;
        int lux = luPos.first, luy = luPos.second, rdx = rdPos.first, rdy = rdPos.second,
            mode = luy == rdy, val = robotBoard[lux][luy][mode]+1;
        bfsQueue.pop();
        
        for(int cnt=0; cnt<4; ++cnt){
            int lunx = lux + dx[cnt], luny = luy + dy[cnt],
                rdnx = rdx + dx[cnt], rdny = rdy + dy[cnt];
            pii lunPos = make_pair(lunx,luny), rdnPos = make_pair(rdnx,rdny);
            
            if(board[lunx][luny] && board[rdnx][rdny]){
                if(!robotBoard[lunx][luny][mode]){
                    robotBoard[lunx][luny][mode] = val;
                    bfsQueue.push(make_pair(lunPos,rdnPos));
                }
            
                if(cnt/2 ^ !mode){ // == (cnt>1 && mode) || (cnt<=1 && !mode)
                    if(cnt%2){ //cnt : 1, 3
                        if(!robotBoard[lunx][luny][!mode]){
                            robotBoard[lunx][luny][!mode] = val;
                            bfsQueue.push(make_pair(lunPos, luPos));
                        }
                        if(!robotBoard[rdnx][rdny][!mode]){
                            robotBoard[rdnx][rdny][!mode] = val;
                            bfsQueue.push(make_pair(rdnPos, rdPos));
                        }
                    }
                    else{ //cnt : 0, 2
                        if(!robotBoard[lux][luy][!mode]){
                            robotBoard[lux][luy][!mode] = val;
                            bfsQueue.push(make_pair(luPos, lunPos));
                        }
                        if(!robotBoard[rdx][rdy][!mode]){
                            robotBoard[rdx][rdy][!mode] = val;
                            bfsQueue.push(make_pair(rdPos, rdnPos));
                        }
                    }
                }
            }
        }
    }
        
    printf("%d",min(robotBoard[n][n-1][0]?robotBoard[n][n-1][0]:1<<30,robotBoard[n-1][n][1]?robotBoard[n-1][n][1]:1<<30)-1);
        
    return 0;
}
