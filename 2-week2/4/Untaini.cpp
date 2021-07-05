#include <cstdio>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int n, srtPtr, endPtr, selItemCnt, resSrt, resEnd, resRange=1000000;
string items[100010];
char itemName[12];
map<string, int> itemCount;
int main() {
	scanf("%d",&n);
	for(int cnt=0;cnt<n;++cnt){
		scanf("%s", itemName);
		items[cnt] = string(itemName);
		if(!itemCount.count(items[cnt]))
			itemCount.insert(make_pair(items[cnt],0));
	}
	
	while(srtPtr<=endPtr && endPtr<=n){
		if(selItemCnt<itemCount.size()){
			if(endPtr == n) break;
			
			if(!itemCount[items[endPtr]]) ++selItemCnt;
			++itemCount[items[endPtr]], ++endPtr;
		}
		else{
			if(endPtr-srtPtr<resRange)
				resSrt = srtPtr, resEnd = endPtr, resRange = endPtr-srtPtr;
			if(!(--itemCount[items[srtPtr]])) --selItemCnt;
			++srtPtr;
		}
	}
	printf("%d\n%d",resSrt+1, resEnd);
	return 0;
}