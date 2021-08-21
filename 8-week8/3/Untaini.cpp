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

bool tracking(int st, int ed, int we){
    if(dp[st] < we) return false;
    else if(st == ed) return true;

    bool isSameTrack = false;
    
    for(int cnt=0; cnt<roads[st].size() && !isSameTrack; ++cnt){
        int next = roads[st][cnt].first, roadWe = roads[st][cnt].second;
        if(dp[st]-roadWe == dp[next])
            isSameTrack |= tracking(next, ed, we);
    }
    
    return isSameTrack;
}

int main() {
    scanf("%d%d%d%d%d",&n,&m,&k,&st,&ed); --st,--ed;
    for(int cnt=0;cnt<k;++cnt){
		       int x; scanf("%d",&x);
		       traps[x-1]=1;
    }
	
	/*
	함정X -> 함정X
	L0 -> R0
	L0 -> R1 추가
	L1 -> R1

	함정O -> 함정X
	L1 -> R0
	R0 -> L1 추가

	함정X -> 함정O
	L0 -> R0
	R0 -> L1 추가
	R0 -> L0

	함정O -> 함정O
	L1 -> R0
	R0 -> L0
	L0 -> R1 추가
	R1 -> L1 추가
	*/
	
    for(int cnt=0;cnt<m;++cnt){
        int x,y,w; scanf("%d%d%d",&x,&y,&w); --x,--y;
        if(traps[x]){
            roads[x+1000].push_back(make_pair(y,w));
            if(traps[y]){
                roads[y].push_back(make_pair(x,w));
                roads[x].push_back(make_pair(y+1000,w));
                roads[y+1000].push_back(make_pair(x+1000,w));
            }
            else
                roads[y].push_back(make_pair(x+1000,w));
        }
        else{
            roads[x].push_back(make_pair(y,w));
            if(traps[y]){
                roads[y].push_back(make_pair(x,w));
                roads[y].push_back(make_pair(x+1000,w));
            }
            else{
                roads[x].push_back(make_pair(y+1000,w));
                roads[x+1000].push_back(make_pair(y+1000,w));
            }
        }
    }
	
    for(int cnt=0;cnt<2000;++cnt)
        dp[cnt]=1e9;
	
    pq.push(make_pair(0,st));
	
    while(!pq.empty()){
        int weight = pq.top().first, node = pq.top().second;
        pq.pop();
		        
        if(dp[node]!=1e9) continue;
        dp[node] = weight;
        
        //printf("%d %d\n", node, -weight);
        
        for(int cnt=0; cnt<roads[node].size(); ++cnt){
            int roadWeight = roads[node][cnt].second, nextNode = roads[node][cnt].first;
            
            if(nextNode>=1000){
                if(node>=1000 && !traps[node-1000] && !traps[nextNode-1000])
                    pq.push(make_pair(weight-roadWeight,nextNode));
                else if(tracking(nextNode-1000,node,weight))
                    pq.push(make_pair(weight-roadWeight,nextNode));
            }
            else
                pq.push(make_pair(weight-roadWeight,nextNode));
        }
    }
	
	
    printf("%d",dp[ed]==1e9?-1:-dp[ed]);
    return 0;
}
