#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main()
{
	int n, k;
	cin >> n >> k;

	int* moves = new int[k];
	queue<int>* board = new queue<int>[n];

	for (int i = 0; i < k; i++)
		cin >> moves[i];
	int temp;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> temp;
			if (temp != 0)
				board[j].push(temp);
		}
	}

	vector<int> basket = { 0 };
	int move, p;
	int count = 0;
	for (int i = 0; i < k; i++) {
		move = moves[i] - 1;
		if (board[move].empty() == false) {
			p = board[move].front();
			board[move].pop();
			if (p == basket.back()) {
				count += 2;
				basket.pop_back();
			}
			else
				basket.push_back(p);
		}
	}

	cout << count << endl;

	return 0;
}