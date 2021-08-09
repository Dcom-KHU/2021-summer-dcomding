#include <cstdio>
#include <stack>
using namespace std;

int n, bCnt;
double sum, avg, m, block;
stack<double> blocks;
int main()
{
    scanf("%d%lf",&n,&m);
    for(int cnt=0; cnt<n; ++cnt){
        scanf("%lf",&block);
        blocks.push(sum=avg=block);
    }
    blocks.pop(); ++bCnt;
    bool isFallen = false;
    
    while(!blocks.empty() && !isFallen){
        block = blocks.top(); blocks.pop();
        isFallen = block-m >= avg || avg >= block+m;
        avg = (sum+=block)/++bCnt;
    }
    
    printf("%d", !isFallen);
    return 0;
}
