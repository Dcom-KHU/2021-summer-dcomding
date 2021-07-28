#include <cstdio>
#include <algorithm>
using namespace std;

#define pii pair<int,int>

int n, f, k, num, delName[1000001], delPtr, fwTree[1000010];
char command;

void update(int num, int val){
    while(num<=n)
        fwTree[num] += val, num += (num & -num);
}

int getSum(int ed){
    int res = 0;
    while(ed)
        res += fwTree[ed], ed -= (ed & -ed);
    return res;
}

int bs(int val){
    int l=1, r=n, m;
    while(l<=r){
        m=(l+r)/2;
        if(getSum(m)<=val) l=m+1;
        else r=m-1;
    }
    return l;
}

int main()
{
    scanf("%d%d%d",&n,&f,&k); ++n, ++f; getchar();
    for(int cnt=1; cnt<n; ++cnt)
        update(cnt, 1);
    
    for(int cnt=0; cnt<k; ++cnt){
        scanf("%c",&command);
        switch(command){
        case 'U':
            scanf("%d",&num); getchar();
            f = bs(getSum(f)-num-1);
        break;
        
        case 'D':
            scanf("%d",&num); getchar();
            f = bs(getSum(f)+num-1);
        break;
        
        case 'C':
            getchar();
            delName[delPtr++] = f;
            update(f, -1);
            if(f==n-1) f = bs(getSum(f)-1);
            else f = bs(getSum(f));
        break;
        
        case 'Z':
            getchar();
            update(delName[--delPtr],1);
        break;
        }
    }
    
    sort(delName, delName+delPtr);
    for(int cnt=0; cnt<delPtr; ++cnt)
        printf("%d\n",delName[cnt]-1);
        
    return 0;
}
