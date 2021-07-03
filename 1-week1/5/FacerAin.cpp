#include <iostream>
#include <algorithm>
using namespace std;

const int MAX = 1000005;

/*
점화식은?
dp[i] -> i번째 노트북을 훔쳤을 때 최대의 가격
dp[i] = max(dp[i-1],dp[i-2]+map[i])

마지막 노트북 처리는?
원형 구조이기 때문에 고려를 해주어야 한다.

*/

int map[MAX];
int dp[MAX];

int main(){
	int n;
	cin >> n;
	for(int i = 0; i < n; i++){
		cin >> map[i];
	}
	dp[0] = 1;
	dp[1] = max(dp[0],map[1]);
	for(int i = 2; i < n; i++){
		dp[i] = max(dp[i-1],dp[i-2]+map[i]);
	}
	if(dp[1] == dp[0]){
		dp[n-1] -= dp[0];
	}
	
	cout << dp[n-1];
	
	return 0;
}