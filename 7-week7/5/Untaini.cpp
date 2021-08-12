#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

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
	
	funcStack.push(make_pair(0,0));
	while(!funcStack.empty()){
		int leader = funcStack.top().first, mode = funcStack.top().second;
		funcStack.pop();
		if(!mode){
			funcStack.push(make_pair(leader,1));
			for(int cnt=0;cnt<tree[leader].size();++cnt)
				funcStack.push(make_pair(tree[leader][cnt],0));
		}
		else{
			int sumMembers = 0;
			for(int cnt=0; cnt<tree[leader].size(); ++cnt){
				member = tree[leader][cnt];
				dp[leader][0] += min(dp[member][0], dp[member][1]), sumMembers += dp[member][0];
			}
			dp[leader][1] = dp[leader][0];
			
			if(tree[leader].size() && dp[leader][0] == sumMembers){
				dp[leader][0] = (1<<31)-1;
				
				for(int cnt=0; cnt<tree[leader].size(); ++cnt){
					member = tree[leader][cnt];
					dp[leader][0] = min(dp[leader][0], sumMembers-dp[member][0]+dp[member][1]);
				}
			}
			
			dp[leader][1] += sales[leader];
		}
	}
	
	printf("%d", min(dp[0][0], dp[0][1]));
	return 0;
}