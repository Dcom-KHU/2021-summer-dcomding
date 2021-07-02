#include <cstdio>

long long result;
int n;

void hanoi(int diskNum, int startPillar, int endPillar, int remainPillar){
	if(diskNum<1) return;
	hanoi(diskNum-1, startPillar, remainPillar, endPillar);
	result+=endPillar;
	hanoi(diskNum-1, remainPillar, endPillar, startPillar);
}

int main() {
	scanf("%d",&n);
	hanoi(n,1,3,2);
	printf("%lld",result);
	return 0;
} 