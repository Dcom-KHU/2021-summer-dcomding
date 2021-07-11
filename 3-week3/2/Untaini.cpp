#include <cstdio>

int n, table[16][2], dp[16][2];

int main() {
	scanf("%d",&n);
	for(int cnt=0;cnt<n;++cnt)
		scanf("%d%d",&table[cnt][0], &table[cnt][1]);
	
	dp[0][0] = table[0][0], dp[0][1] = table[0][1];
	for(int cnt=1;cnt<=n;++cnt){
		int maxVal=0;
		for(int rev = cnt-1; rev>=0; --rev){
			if(cnt<dp[rev][0]) continue;
			maxVal = maxVal>dp[rev][1]?maxVal:dp[rev][1];
		}
		
		dp[cnt][0] = table[cnt][0]+cnt;
		dp[cnt][1] = table[cnt][1]+maxVal;
		
	}
	
	printf("%d",dp[n][1]);
	return 0;
}