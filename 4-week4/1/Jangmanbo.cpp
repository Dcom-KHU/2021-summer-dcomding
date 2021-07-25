#include <iostream>
#include <stack>
#include <string>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int n, k, num;
	queue<int> moves;
	vector<queue<int>> board(6);
	stack<int> stk;

	cin >> n >> k;

	for (int i = 0; i < k; i++)
	{
		cin >> num;
		moves.push(num);
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 1; j <= n; j++)
		{
			cin >> num;
			if (num) board[j].push(num);
		}
	}

	int top, total = 0;
	while (!moves.empty()) {
		num = moves.front();
		moves.pop();
		if (!board[num].empty()) {
			if (stk.empty()) top = 0;
			else top = stk.top();

			if (top == board[num].front() && !stk.empty()) {
				stk.pop();
				total += 2;
			}
			else {
				stk.push(board[num].front());
			}
			board[num].pop();
		}
	}
	cout << total;
	return 0;
}