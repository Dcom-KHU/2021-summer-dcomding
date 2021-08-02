#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int a,b,x,sameElementCnt;
vector<int> aSet;
int main()
{
    scanf("%d%d",&a,&b);
    for(int cnt=0; cnt<a; ++cnt){
        scanf("%d",&x);
        aSet.push_back(x);
    }
    
    for(int cnt=0; cnt<b; ++cnt){
        scanf("%d",&x);
        if(*lower_bound(aSet.begin(), aSet.end(), x) == x) ++sameElementCnt;
    }
    
    printf("%d", a+b-2*sameElementCnt);
    return 0;
}
