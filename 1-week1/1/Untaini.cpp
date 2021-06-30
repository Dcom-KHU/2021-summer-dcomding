#include <cstdio>
#include <algorithm>
using namespace std;

int cardCnt[100001], minPoint=100001, maxPoint, n, k, cardNum, sum;

int main(){
	scanf("%d%d",&n,&k);
	for(int cnt=0;cnt<n;++cnt){
		scanf("%d", &cardNum);
		++cardCnt[cardNum];
		minPoint = min(minPoint, cardNum);
		maxPoint = max(maxPoint, cardNum);
		sum+=cardNum;
	}
	
	for(int cnt=1;cnt<=k;++cnt){
		if(cnt&1){
			while(!cardCnt[minPoint]) ++minPoint;
			sum-=minPoint;
			--cardCnt[minPoint];
		}
		else{
			while(!cardCnt[maxPoint]) --maxPoint;
			sum-=maxPoint;
			--cardCnt[maxPoint];
		}
	}
	printf("%d",sum);
	return 0;
}