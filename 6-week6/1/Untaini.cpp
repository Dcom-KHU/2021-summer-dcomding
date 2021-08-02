#include <cstdio>

long long n, e=1;
int main()
{
    scanf("%lld", &n);
    while(e<=n) e<<=1;
    printf("%lld",e>>1);
    return 0;
}
