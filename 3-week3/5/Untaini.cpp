#include <cstdio>
#include <stack>
#include <algorithm>
using namespace std;

#define pii pair<int, int>

int n, h, result;

//stack.top에는 항상 최고 높이만 존재하게끔 만듦
stack<pii> histograms;

int main() {
	scanf("%d",&n);
	for(int cnt=0;cnt<n;++cnt){
		scanf("%d",&h);
		
		int possiblePtr = cnt;		
		while(!histograms.empty() && h<=histograms.top().first){
			pii histogram = histograms.top(); histograms.pop();
			result = max(result, h*(cnt-histogram.second+1));
			result = max(result, histogram.first*(cnt-histogram.second));
			possiblePtr = histogram.second;
		}
		histograms.push(make_pair(h,possiblePtr));
	}
	
	while(!histograms.empty()){
		pii histogram = histograms.top(); histograms.pop();
		result = max(result, histogram.first*(n-histogram.second));
	}
	printf("%d",result);
	return 0;
}