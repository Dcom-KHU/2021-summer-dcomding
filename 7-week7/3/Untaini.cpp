#include <cstdio>

#define max(a,b) (a>b?a:b)

//sumCookies : 1~n까지 쿠키의 누적합
int n, cookie, sumCookies[2001], res;

//[a,b], [b+1,c]중 b를 담당하는 이진 탐색
//a,c가 정해져 있으면 각 구간의 합이 동일하게 만드는 b는 여러개라도 동일한 구간의 합의 값은 단 1개이다.
//또한 f(x) = [a,x] - [x+1,c]로 두면 f(x)는 증가함수 이므로 이를 이용해 이진탐색이 가능하다.
int binary_search(int eLeft, int eRight){
	
	//rSum = [1,eRight] - [1,eLeft], 즉, [1,c] - [1,a-1] = [a,c] // mid가 b의 역할을 함
	int left = eLeft+1, right = eRight, mid, lSum, rSum = sumCookies[eRight]-sumCookies[eLeft];
	
	while(left<=right){
		//lSum = [1,b] - [1,a-1] = [a,b]
		mid = (left+right)/2, lSum = sumCookies[mid]-sumCookies[eLeft];
		
		//[a,b] == [b+1,c] ==> [a,b] == [a,c]-[a,b] ==> 2*[a,b] == [a,c]
		if(2*lSum == rSum) return lSum;
		else if(2*lSum > rSum) right = mid-1;
		else left = mid+1;
	}
	return -1;
}

int main() {
	scanf("%d",&n);
	//[a,b], [b+1,c]중 c를 담당하는 for문
	for(int cnt=1; cnt<=n; ++cnt){
		scanf("%d",&cookie);
		//값을 입력 받으면서 바로 구간합을 갱신함
		sumCookies[cnt] = sumCookies[cnt-1]+cookie;
		
		//[a,b], [b+1,c]중 a를 담당하는 for문, srtBasket == a-1임
		for(int srtBasket = 0; srtBasket<cnt; ++srtBasket){
			//binary search를 이용해서 구간의 합을 찾고 답을 갱신함
			res = max(res, binary_search(srtBasket, cnt));
		}
	}
	
	printf("%d", res);
	
	return 0;
}