#include <cstdio>

int n;

int main()
{
    scanf("%d",&n);
    while(n != (n & -n)) n -= (n & -n);
    printf("%d",n);
    return 0;
}
