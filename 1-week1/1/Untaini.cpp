#include <cstdio>
#include <deque>
#include <algorithm>
using namespace std;


long long sumResult;
deque<int> numCards;
int n, k, num;

int main(){
	scanf("%d%d",&n,&k);
	for(int cnt=0;cnt<n;++cnt){
		scanf("%d",&num);
		numCards.push_back(num);
		sumResult += num;
	}
	
	sort(numCards.begin(), numCards.end());
	
	for(int cnt=1;cnt<=k;++cnt)
		if(cnt&1){
			sumResult -= numCards.front();
			numCards.pop_front();
		}
		else{
			sumResult -= numCards.back();
			numCards.pop_back();
		}
	
	printf("%lld", sumResult);
	return 0;
}