#include <iostream>

using namespace std;

int N;
int A[11];
int res[2] = {1000000001,-1000000000};
int Opr[4] = { 0, };

void Get_Res(int cur, int cnt) {
	if (cnt == N) {
		if (res[0] > cur ) {
			res[0] = cur;
		}
		if (res[1] < cur) {
			res[1] = cur;
		}
		return;
	}

	if (Opr[0]) {
		Opr[0]--;
		Get_Res(cur + A[cnt], cnt + 1);
		Opr[0]++;
	}
	if (Opr[1]) {
		Opr[1]--;
		Get_Res(cur - A[cnt], cnt + 1);
		Opr[1]++;
	}
	if (Opr[2]) {
		Opr[2]--;
		Get_Res(cur * A[cnt], cnt + 1);
		Opr[2]++;
	}
	if (Opr[3]) {
		Opr[3]--;
		Get_Res(cur / A[cnt], cnt + 1);
		Opr[3]++;
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int input;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	for (int i = 0; i < 4; i++) {
		cin >> input;
		Opr[i] = input;
	}

	Get_Res(A[0], 1);
	cout << res[1] << "\n" << res[0];
}