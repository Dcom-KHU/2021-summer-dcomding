#include <cstdio>

#define min(a,b) (a<b?a:b)

int arrows[2], prevArr;
char arrStr[1000001];
int main()
{
    scanf("%s",arrStr);
    prevArr = arrStr[0];
    for(int cnt=1; arrStr[cnt-1]; ++cnt){
        if(prevArr != arrStr[cnt]) ++arrows[prevArr-'0'];
        prevArr = arrStr[cnt];
    }
    
    printf("%d", min(arrows[0], arrows[1]));
        
    return 0;
}
