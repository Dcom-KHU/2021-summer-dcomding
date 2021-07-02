#include <cstdio>

unsigned long long result=1, expTwo=1;
int n;

//1 <= n <= 62 계산 가능
//식은.. 원반이 처음에 위치한 자리에 따리 거쳐가는 막대의 경로가 같기 때문에
//그것을 이용한 O(1)의 일반향입니다.. f(n) = n + 2^(n+1) - 2
int main() {
	scanf("%d",&n);
	result<<=n+1;
	printf("%llu",n+result-2);
	return 0;
}