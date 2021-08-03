#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

#define pii pair<int, int>
#define abs(a) (a>0?a:-a)

int n, weights[200000], a, b, res;
bool visited[200000]={1};
vector<vector<int>> tree(200000, vector<int>());
queue<int> bfsQueue;
stack<pii> calcEdges;
int main()
{
    scanf("%d",&n);
    for(int cnt=0; cnt<n; ++cnt)
        scanf("%d",&weights[cnt]);
     
    for(int cnt=1; cnt<n; ++cnt){
        scanf("%d%d",&a,&b);
        tree[a].push_back(b);
        tree[b].push_back(a);
    }
    
    bfsQueue.push(0);
    while(!bfsQueue.empty()){
        int node = bfsQueue.front(); bfsQueue.pop();
        for(int cnt=0; cnt<tree[node].size(); ++cnt){
            int nextNode = tree[node][cnt];
            if(!visited[nextNode]){
                ++visited[nextNode]; 
                bfsQueue.push(nextNode);
                calcEdges.push(make_pair(node, nextNode));
            }
        }
    }
    
    while(!calcEdges.empty()){
        int pNode =calcEdges.top().first, cNode = calcEdges.top().second;
        calcEdges.pop();
        res += abs(weights[cNode]), weights[pNode] += weights[cNode];
    }
    
    printf("%d", weights[0]?-1:res);
    return 0;
}
