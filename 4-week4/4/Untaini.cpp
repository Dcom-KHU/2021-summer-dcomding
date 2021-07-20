#include <cstdio>

int n, l, map[101][101], dx[]={1,0}, dy[]={0,1}, result;

bool canCrossRoad(int row, int col, int mode){
    int cnt=0, prevHeight=map[row][col];
    while(row<n && col<n){
        switch(prevHeight-map[row][col]){
            case 1: 
                if(cnt<0) return false;
                cnt=1-l;
            break;
            
            case 0: ++cnt; break;
            
            case -1:
                if(cnt<l) return false;
                cnt=1;
            break;
            
            default: return false;
        }
        prevHeight = map[row][col];
        row+=dy[mode], col+=dx[mode];
    }
    return cnt>=0;
}

int main()
{
    scanf("%d%d",&n,&l);
    for(int row=0; row<n; ++row)
        for(int col=0; col<n; ++col)
            scanf("%d",&map[row][col]);
            
    for(int cnt=0; cnt<n; ++cnt)
        result += canCrossRoad(cnt, 0, 0) + canCrossRoad(0, cnt, 1);
        
    printf("%d", result);
    return 0;
}
