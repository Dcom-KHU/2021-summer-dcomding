#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

#define pii pair<int, int>


int n,t,m,k, hour, minute, busCnt;
priority_queue<pii,vector<pii>, greater<pii>> students;
pii bus=make_pair(9,0), mustGo;

int main() {
	scanf("%d%d%d%d",&n,&t,&m,&k);
	for(int cnt=0;cnt<k;++cnt){
		scanf("%d%d",&hour,&minute);
		students.push(make_pair(hour,minute));
	}
	
	
	while(n-->0){
		busCnt=0;
		mustGo = bus;
		while(!students.empty() && bus>=students.top() && busCnt<m){
			mustGo = students.top(); students.pop();
			mustGo.first -= !mustGo.second, mustGo.second = (mustGo.second+59)%60;
			++busCnt;
		}
		if(n) bus.first += (bus.second+t)/60, bus.second = (bus.second+t)%60;
	}
	
	if(busCnt==m)
		printf("%d %d", mustGo.first, mustGo.second);
	else
		printf("%d %d", bus.first, bus.second);
	
	
	return 0;
}