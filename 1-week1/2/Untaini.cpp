#include <cstdio>

long long result;
int n;


int main() {
	scanf("%d",&n);
	for(int i=1;i<=n;++i)
		if((n-i)&1)
			result += (1<<n-i+1) + ((1<<n-i)%3!=1?3-(1<<n-i)%3:0);
		else
			result += (1<<(n-i+1)) + 1;
		
	printf("%lld",result);
	return 0;
}