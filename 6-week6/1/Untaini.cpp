#include <cstdio>

int n,alive;

int main()
{
    scanf("%d",&n);
    while(n) n ^= (alive = n & -n);
    printf("%d",alive);
    return 0;
}
