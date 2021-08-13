#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

//dp[n] : n을 루트로 하는 서브 트리에서 ([0] : n을 포함하지 않고, [1] : n을 포함하고) 서브 트리의 모든 팀을 참여시킬 때의 매출액의 최솟값
int n, sales[300001], leader, member, dp[300001][2];
vector<vector<int>> tree(300001,vector<int>());
stack<pair<int, int>> funcStack;

int main(){
	scanf("%d",&n);
	for(int cnt=0;cnt<n;++cnt)
		scanf("%d",&sales[cnt]);
	
	for(int cnt=1;cnt<n;++cnt){
		scanf("%d%d",&leader,&member);
		tree[leader].push_back(member);
	}
	
	//재귀함수 대신 funcStack 사용
	funcStack.push(make_pair(0,0));
	while(!funcStack.empty()){
		int leader = funcStack.top().first, mode = funcStack.top().second;
		funcStack.pop();
		
		//mode가 0일 때는 재귀적으로 각 서브 트리로 진입함
		if(!mode){
			funcStack.push(make_pair(leader,1));
			for(int cnt=0;cnt<tree[leader].size();++cnt)
				funcStack.push(make_pair(tree[leader][cnt],0));
		}
		
		//mode가 1일 때 팀원노드들은 모두 계산이 완료되어 있으므로 팀장노드를 계산함
		else{
			//팀장 노드가 들어갈 때(dp[leader][1])는 항상 팀장의 팀이 들어가니까
			//팀원들이 들어가든 말든 상관없이 (팀원하위팀 매출액 최솟값의 합 + 팀장 매출액) 이 최솟값이 됨

			//팀장 노드가 들어가지 않을 때(dp[leader][0])는 팀원 1명 이상이 무조건 들어가 있어야 하니
			//sumMembers를 이용해서 예외상황을 처리함
			int sumMembers = 0;
			for(int cnt=0; cnt<tree[leader].size(); ++cnt){
				member = tree[leader][cnt];
				dp[leader][0] += min(dp[member][0], dp[member][1]), sumMembers += dp[member][0];
			}
			dp[leader][1] = dp[leader][0]+sales[leader];
			
			//dp[leader][0]은 현재 (팀원하위팀 매출액 최솟값의 합)이기 때문에 이게 sumMembers이랑 같다는 건
			//팀원이 한명도 들어가 있지 않다고 추측할 수 있음
			if(tree[leader].size() && dp[leader][0] == sumMembers){
				
				//따라서 팀원을 한 명씩 넣어보면서 최솟값을 갱신함 
				dp[leader][0] = (1<<31)-1;
				for(int cnt=0; cnt<tree[leader].size(); ++cnt){
					member = tree[leader][cnt];
					dp[leader][0] = min(dp[leader][0], sumMembers-dp[member][0]+dp[member][1]);
				}
			}
		}
	}
	
	//CEO가 들어간 최솟값과 제외한 최솟값 중 더 작은 값을 출력함
	printf("%d", min(dp[0][0], dp[0][1]));
	return 0;
}