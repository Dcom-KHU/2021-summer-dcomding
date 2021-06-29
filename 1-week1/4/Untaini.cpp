#include <cstdio>
#include <algorithm>
using namespace std;

#define INT_MAX (1<<31)-1

//n,k,stones는 입력받는 값을 저장할 변수, rangeMaxTree, pnt(=point)는 세그먼트 트리를 구현하기 위한 변수 / <<X는 *(2의 X제곱)과 같음.
int n,k,stones[200020], rangeMaxTree[1<<21], pnt=1;

//세그먼트 트리를 업데이트 하는 함수
void update(int node, int value){
	//node에 point를 더해 세그먼트 트리의 리프노드를 향하게 만들고
	//리프노드는 구간이 하나니까 max값을 계산하는 대신 값을 그대로 저장함
	node += pnt; 
	rangeMaxTree[node] = value;
	
	//그 뒤로 루트노드까지 노드의 부모노드를 방문해서 max값을 재계산함.
	while(node/=2)
		rangeMaxTree[node] = max(rangeMaxTree[node*2], rangeMaxTree[node*2+1]); 
}

int getRangeMax(int srt, int end){
	//구간의 시작과 끝점에 point를 더해 세그먼트 트리의 리프노드를 향하게 만듦 + 초기값 세팅
	srt += pnt, end += pnt;
	int maxNum = 0;
	
	//리프노드들부터 올라가면서 구간의 max값을 구함.
	while(srt<=end){
		
		//start가 홀수일 때 더 이상 합칠 구간이 없으므로 max값에 반영 후 start 한 칸 오른쪽으로 이동
		if(srt&1) maxNum = max(maxNum,rangeMaxTree[srt++]);
		
		//end가 짝수일 때 더 이상 합칠 구간이 없으므로 max값에 반영 후 end 한 칸 왼쪽으로 이동
		if(!end&1) maxNum = max(maxNum, rangeMaxTree[end--]);
		
		//start와 end 모두 부모노드로 올라감. >>=X는 /=(2의 X제곱)과 같음.
		srt>>=1, end>>=1;
	}
	return maxNum;
}


// 알고리즘
// n번째 징검다리에서 건널 수 있는 최대 인원수 = (n-k~n-1번째 징검다리에서 건널 수 있는 최대 인원수) 와 (n번째 징검다리에서 건널 수 있는 인원수) 중 최솟값
// 이라 생각하고 구현했습니당
// 세그먼트 트리는 이 때 [n-k,n-1] 구간의 최댓값을 빨리 구하려고 만드는 것

int main(){
	scanf("%d%d",&n,&k);
	for(int cnt=1; cnt<=n; ++cnt)
		scanf("%d", &stones[cnt]);
	
	//point가 가리킬 위치를 계산하는 것, 세그먼트 트리를 완전 이진 트리로 만들어서 계산에 용이하도록 만듦 
	while(pnt<=n) pnt<<=1;
	
	
	update(0, INT_MAX);//INT_MAX는 #define 참고, 처음(0번째 징검다리 = 지상)에는 무제한으로 건너올 수 있으니까 반영함
	for(int dpCnt=1; dpCnt<=n; ++dpCnt){
		//maxNum : 구간 중 건널 수 있는 최대 인원수, possibleMember = dpCnt번째 징검다리에서 건널 수 있는 최대 인원수
		int maxNum = getRangeMax(max(0,dpCnt-k), dpCnt-1),
			possibleMember = min(stones[dpCnt], maxNum);
		
		//다음 계산을 위해 세그먼트 트리에 반영
		update(dpCnt, possibleMember);
		
		//한 줄로 바꾸면 아래가 됨
		//update(dpCnt, min(getRangeMax(max(0,dpCnt-k),dpCnt-1), stones[dpCnt]));
	}
	
	//도착지점에서의 구간 최댓값을 구하면 원하는 결과를 얻을 수 있음
	printf("%d",getRangeMax(n-k+1,n));
	return 0;
}