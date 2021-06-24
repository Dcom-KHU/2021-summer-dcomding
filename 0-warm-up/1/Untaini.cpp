#include <cstdio>

int num, cnt;
int main() {
	scanf("%d",&num);
	for(cnt=1;cnt<=3;++cnt)
		printf("%d * %d = %d\n",num,cnt,num*cnt);
	return 0;
}