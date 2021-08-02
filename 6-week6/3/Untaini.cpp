#include <cstdio>
#include <stack>
#include <algorithm>
using namespace std;

#define pii pair<int, int>

int n,m, map[501][501], course[501][501], dx[]={1,-1,0,0}, dy[]={0,0,1,-1};
bool visited[501][501];
stack<pair<int, pii>> funcStack;

bool canMove(int x, int y){
    return 0<=x && x<n && 0<=y && y<m;
}

int main()
{
    scanf("%d%d",&n,&m);
    for(int nCnt=0; nCnt<n; ++nCnt)
        for(int mCnt=0; mCnt<m; ++mCnt)
            scanf("%d",&map[nCnt][mCnt]);
            
    funcStack.push(make_pair(0,make_pair(0,0)));
    course[n-1][m-1] = visited[n-1][m-1] = 1;
    
    while(!funcStack.empty()){
        pii pos = funcStack.top().second;
        int type = funcStack.top().first, x = pos.first, y = pos.second;
        funcStack.pop();
        
        if(visited[x][y]) continue;
        
        if(!type){
            funcStack.push(make_pair(1,pos));
            for(int cnt=0; cnt<4; ++cnt){
                int nx = x+dx[cnt], ny = y+dy[cnt];
                if(canMove(nx,ny) && !course[nx][ny] && map[x][y] > map[nx][ny])
                    funcStack.push(make_pair(0,make_pair(nx,ny)));
            }
        }
        else{
            for(int cnt=0; cnt<4; ++cnt){
                int nx = x+dx[cnt], ny = y+dy[cnt];
                if(canMove(nx,ny) && map[x][y] > map[nx][ny])
                    course[x][y] += course[nx][ny];
            }
            visited[x][y] = 1;
        }
    }
    
    printf("%d",course[0][0]);
    return 0;
}
