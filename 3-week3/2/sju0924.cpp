// boj14501(퇴사).cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>

using namespace std;
int T[16] = { 1,0, }, P[16], N, res = 0;

void getMaxProfit(int day, int point) {
	int t = T[day];
	int p = P[day];	

	if(day<=N) getMaxProfit(day + 1, point);
	if (day + t <= N) {
		getMaxProfit(day + t,point + p);		
	}
	else if (day + t == N + 1) { // 종료 날짜에 딱 맞춰서 끝냄
		if (res < point + p) res = point + p;
		return;
	}
	else {
		if (res < point) res = point;
		return;
	}
}
int main()
{
	cin >> N;

	for (int i = 1; i <= N; i++) {
		cin >> T[i] >> P[i];
	}

	getMaxProfit(1, 0);

	cout << res;
}