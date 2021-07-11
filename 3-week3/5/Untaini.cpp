#include <cstdio>
#include <stack>
#include <algorithm>
using namespace std;

#define pii pair<int, int>

int n, h, result;

//histograms에는 항상 오름차순 높이만 존재하게끔 만듦 (뽑을 때는 내림차순으로 나옴)
stack<pii> histograms;

int main() {
	scanf("%d",&n);
	for(int cnt=0;cnt<n;++cnt){
		scanf("%d",&h);
		
		int possiblePtr = cnt;		
		while(!histograms.empty() && h<=histograms.top().first){
			pii histogram = histograms.top(); histograms.pop();
			
			//현재 높이에서 가능한 넓이와 result를 비교함
			result = max(result, h*(cnt-histogram.second+1));
			
			//스택에 있던 first는 현재 높이 h에서는 불가능하므로 h이전 위치까지의 넓이와 result를 비교함
			//이게 가능한 이유는 histograms가 오름차순으로 들어가 있기 때문에 넓이가 보장됨.
			result = max(result, histogram.first*(cnt-histogram.second));
			
			//h보다 크거나 같은 높이값이기 때문에 second(=first 높이의 시작점)부터 최소 h만큼의 높이를 보장함
			possiblePtr = histogram.second;
		}
		histograms.push(make_pair(h,possiblePtr));
	}
	
	//마지막으로 스택에서 빠지지 않은 (높이,시작점)들을 빼면서 최대값을 갱신함.
	while(!histograms.empty()){
		pii histogram = histograms.top(); histograms.pop();
		result = max(result, histogram.first*(n-histogram.second));
	}
	
	printf("%d",result);
	return 0;
}