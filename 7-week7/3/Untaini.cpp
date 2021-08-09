#include <cstdio>

#define max(a,b) (a>b?a:b)

int n, cookie, sumCookies[2001], res;

int binary_search(int eLeft, int eRight){
	int left = eLeft+1, right = eRight, mid, lSum, rSum = sumCookies[eRight]-sumCookies[eLeft];
	while(left<=right){
		mid = (left+right)/2, lSum = sumCookies[mid]-sumCookies[eLeft];
		if(2*lSum == rSum) return lSum;
		else if(2*lSum > rSum) right = mid-1;
		else left = mid+1;
	}
	return -1;
}

int main() {
	scanf("%d",&n);
	for(int cnt=1; cnt<=n; ++cnt){
		scanf("%d",&cookie);
		sumCookies[cnt] = sumCookies[cnt-1]+cookie;
		for(int srtBasket = 0; srtBasket<cnt; ++srtBasket){
			res = max(res, binary_search(srtBasket, cnt));
		}
	}
	
	printf("%d", res);
	
	return 0;
}