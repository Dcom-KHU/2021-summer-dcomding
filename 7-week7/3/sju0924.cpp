#include <string>
#include <vector>
#include<algorithm>
#include<iostream>

using namespace std;

vector<vector<int>> cookies(2001,vector<int>(2001));
int cookie[2001];
int main() {

	int input,n;

	int answer = 0;

	cin >> n;
	for (int i = 1; i <= n;i++) {
		cin >> cookie[i];
	}
	for (int i = 1; i <= n;i++) {
		cookies[i][i] = cookie[i];
		for (int j = i + 1;j <= n;j++) {
			cookies[i][j] = cookies[i][j - 1] + cookie[j];
		}
	}

	for (int i = 1; i <= n;i++) {
		for (int j = i;j < n;j++) {
			if (cookies[i][j] <= answer) continue;
			if (cookies[i][j] > cookies[j + 1][n]) continue;
			if (find(cookies[j+1].begin(),cookies[j+1].end(),cookies[i][j]) != cookies[j+1].end()) {
				if (cookies[i][j] > answer) {
					answer = cookies[i][j];
					}
			}
		}
	}
	cout << answer;

	//return answer;
}