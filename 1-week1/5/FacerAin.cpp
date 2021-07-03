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
int n;
void print_dp(){
	for(int i = 0; i < n; i++){
		cout << dp[i] << endl;
	}
}
int main(){

	cin >> n;
	for(int i = 0; i < n; i++){
		cin >> map[i];
	}
	dp[0] = map[0];
	dp[1] = max(dp[0], map[1]);
	for(int i = 2; i < n-1; i++){
		dp[i] = max(dp[i-1],dp[i-2]+map[i]);
	}
	int ans1 = dp[n-2];//마지막 제외
	
	dp[0] = 0;
	dp[1] = map[1];
	for(int i = 2; i < n; i++){
		dp[i] = max(dp[i-1],dp[i-2]+map[i]);
	}
	int ans2 = dp[n-1];//첫번째 제외
	
	cout << max(ans1, ans2);
	return 0;
}