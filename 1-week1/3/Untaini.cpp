#include <cstdio>
#include <algorithm>
using namespace std;

int n, numList[12], operatorCntList[4], minResult=(1<<31)-1, maxResult=1<<31;

void operateFunc(int cnt, int prevResult){
	if(cnt==n){
		minResult = min(minResult, prevResult);
		maxResult = max(maxResult, prevResult);
	}
	else{
		for(int opeCnt=0; opeCnt<4; ++opeCnt){
			if(operatorCntList[opeCnt]){
				--operatorCntList[opeCnt];
				switch(opeCnt){
					case 0: operateFunc(cnt+1, prevResult+numList[cnt]); break;
					case 1: operateFunc(cnt+1, prevResult-numList[cnt]); break;
					case 2: operateFunc(cnt+1, prevResult*numList[cnt]); break;
					case 3: operateFunc(cnt+1, prevResult/numList[cnt]); break;
				}
				++operatorCntList[opeCnt];
			}
		}
	}
}

int main() {
	scanf("%d",&n);
	for(int cnt=0; cnt<n; ++cnt)
		scanf("%d",&numList[cnt]);
	for(int cnt=0; cnt<4; ++cnt)
		scanf("%d",&operatorCntList[cnt]);
	
	operateFunc(1,numList[0]);
	printf("%d\n%d",maxResult,minResult);
	return 0;
} 