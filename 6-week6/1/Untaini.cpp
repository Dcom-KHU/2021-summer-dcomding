#include <cstdio>

int n, e=1;
int main()
{
    scanf("%d", &n);
    while(e<=n) e<<=1;
    printf("%d",e>>1);
    return 0;
}
