#include <cstdio>
#include <algorithm>
using namespace std;

int n,money[1000010],selLastNote[1000010][2], exceptLastNote[1000010][2];

int main() {
	scanf("%d",&n);
	for(int cnt=0;cnt<n;++cnt)
		scanf("%d",&money[cnt]);

	exceptLastNote[0][1] = money[0];
	
	for(int dpCnt=1; dpCnt<=n; ++dpCnt){
		selLastNote[dpCnt][0] = max(selLastNote[dpCnt-1][0], selLastNote[dpCnt-1][1]);
		selLastNote[dpCnt][1] = selLastNote[dpCnt-1][0] + money[dpCnt];
		
		exceptLastNote[dpCnt][0] = max(exceptLastNote[dpCnt-1][0], exceptLastNote[dpCnt-1][1]);
		exceptLastNote[dpCnt][1] = exceptLastNote[dpCnt-1][0] + money[dpCnt];
	}
	
	printf("%d", max(selLastNote[n][0], exceptLastNote[n-1][0]));
	return 0;
}