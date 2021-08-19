#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

#define pii pair<int,int>

int n,m,k,st,ed,dp[2000];
bool traps[1000];
vector<vector<pii>> roads(2000, vector<pii>());
priority_queue<pii> pq; //<-weight, node>

int main() {
	scanf("%d%d%d%d%d",&n,&m,&k,&st,&ed); --st,--ed;
	for(int cnt=0;cnt<k;++cnt){
		int x; scanf("%d",&x);
		traps[x-1]=1;
	}
	
	for(int cnt=0;cnt<m;++cnt){
		int x,y,w; scanf("%d%d%d",&x,&y,&w); --x,--y;
		if(traps[x]){
			roads[x+1000].push_back(make_pair(y,w));
			if(traps[y])
				roads[y].push_back(make_pair(x,w));	
		}
		else{
			roads[x].push_back(make_pair(y,w));
			if(traps[y])
				roads[y].push_back(make_pair(x,w));
			else
				roads[x+1000].push_back(make_pair(y+1000,w));	
		}
	}
	
	for(int cnt=0;cnt<=2000;++cnt)
		dp[cnt]=1e9;
	
	pq.push(make_pair(0,st));
	
	while(!pq.empty()){
		int weight = pq.top().first, node = pq.top().second;
		pq.pop();
		
		if(dp[node]!=1e9) continue;
		dp[node] = weight;
		
		for(int cnt=0; cnt<roads[node].size(); ++cnt){
			int roadWeight = roads[node][cnt].second, nextNode = roads[node][cnt].first;
			if(traps[node%1000]){
				if(traps[nextNode%1000] && node<1000)
					roads[nextNode].push_back(make_pair(node+1000,roadWeight));
				pq.push(make_pair(weight-roadWeight,nextNode));
			}
			else{
				if(traps[nextNode%1000])
					roads[nextNode].push_back(make_pair(node+1000,roadWeight));
				
				else if(node<1000 && dp[nextNode]!=1e9)
					pq.push(make_pair(weight-roadWeight,nextNode+1000));
				
				pq.push(make_pair(weight-roadWeight,nextNode));
			}
		}
	}
	
	
	printf("%d",dp[ed]==1e9?-1:-dp[ed]);
	return 0;
}