#include <cstdio>

int a,b,aList[1000000],x,sameElementCnt;

bool bs(int val){
    int l=0, r=a-1, m;
    while(l<=r){
        m = (l+r)/2;
        if(aList[m] == val) return 1;
        else if(aList[m] > val) r=m-1;
        else l=m+1;
    }
    return 0;
}

int main()
{
    scanf("%d%d",&a,&b);
    for(int cnt=0; cnt<a; ++cnt)
        scanf("%d",&aList[cnt]);
    
    for(int cnt=0; cnt<b; ++cnt){
        scanf("%d",&x);
        if(bs(x)) ++sameElementCnt;
    }
    
    printf("%d", a+b-2*sameElementCnt);
    return 0;
}
