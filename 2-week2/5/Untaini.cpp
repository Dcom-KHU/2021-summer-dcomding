#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

#define pii pair<int, int>
#define piiii pair<pii, pii>

int n, arrow, x, y, dx[] = {1,0,-1}, dy[]={1,0,-1}, result;
set<pii> visitedLocSet;
set<piiii> drewEdgeSet;
vector<piiii> edgeList;
pii prevVertex = make_pair(0,0), nextVertex;
piiii edge;

int main() {
	scanf("%d", &n);
	for(int cnt=0; cnt<n; ++cnt){
		scanf("%d",&arrow);
		x += dx[!(arrow%4) + 2*(arrow>4)];
		arrow = (arrow+2)%8;
		y += dy[!(arrow%4) + 2*(arrow>4)];
		
		
		nextVertex = make_pair(x, y);
		edge = make_pair(min(prevVertex, nextVertex), max(prevVertex, nextVertex));
		if(!drewEdgeSet.count(edge)) {
			drewEdgeSet.insert(edge);
			edgeList.push_back(edge);
		}
		prevVertex = nextVertex;
		
	}
	
	for(int cnt=0; cnt<edgeList.size(); ++cnt){
		prevVertex = edgeList[cnt].first, nextVertex = edgeList[cnt].second;
		bool visitedPrevVertex = visitedLocSet.count(prevVertex), visitedNextVertex = visitedLocSet.count(nextVertex);
		
		if(visitedPrevVertex && visitedNextVertex) ++result;
		
		if(!visitedPrevVertex) visitedLocSet.insert(prevVertex);
		if(!visitedNextVertex) visitedLocSet.insert(nextVertex);
	}
	
	printf("%d",result);
	
	return 0;
}