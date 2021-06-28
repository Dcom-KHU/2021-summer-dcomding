#include <cstdio>
#include <algorithm>
using namespace std;

int n,k,stones[200020], rangeMaxTree[1<<21], pnt=1;

void update(int node, int value){
	node += pnt;
	rangeMaxTree[node] = value;
	while(node/2){
		node/=2;
		rangeMaxTree[node] = max(rangeMaxTree[node*2], rangeMaxTree[node*2+1]);
	}
}

int getRangeMax(int srt, int end){
	srt += pnt, end += pnt;
	int maxNum = 0;
	while(srt<=end){
		if(srt%2) maxNum = max(maxNum,rangeMaxTree[srt++]);
		if(!end%2) maxNum = max(maxNum, rangeMaxTree[end--]);
		srt>>=1, end>>=1;
	}
	return maxNum;
}

int main(){
	scanf("%d%d",&n,&k);
	for(int cnt=1; cnt<=n; ++cnt)
		scanf("%d", &stones[cnt]);
	while(pnt<=n) pnt<<=1;
	
	
	update(0, 2147483647);
	for(int dpCnt=1; dpCnt<=n; ++dpCnt){
		int maxNum = getRangeMax(max(0,dpCnt-k),dpCnt-1), possibleMember = stones[dpCnt];
		possibleMember = min(possibleMember, maxNum);
		update(dpCnt, possibleMember);
	}
	printf("%d",getRangeMax(n-k+1,n));
	return 0;
}