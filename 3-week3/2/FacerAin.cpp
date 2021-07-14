#include <iostream>
#include <algorithm>
using namespace std;


int t[20];
int p[20];
int dp[20];
int main(){
	int n;
	cin >> n;
	for(int i = 1; i <= n; i++){
		int a, b;
		cin >> t[i] >> p[i];
		
	}
	
	for(int i = 1; i <= n+1; i++){
		if(t[i] + i <= n+1){
			dp[i+t[i]] = max(dp[i+t[i]], dp[i] + p[i]);//SKIP, 지금 하기
			
		}
		dp[i+1] = max(dp[i], dp[i+1]);	
		
	};
	cout << dp[n+1];
	return 0;
	
}