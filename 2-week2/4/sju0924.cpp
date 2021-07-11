// 앱등이.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include<map>
#include<string>
using namespace std;

int pow2(int r) {
	int res = 1;
	for (int i = 0; i < r; i++) {
		res *= 2;
	}
	return res;
}

int tree[17 << 2][100000];
map<string, int>itemnum;
int amount = 0;

void print(int r) {
	int temp;
	for (int i = 1; i < pow2(r + 1);i++) {
		temp = i + 1;

		cout << "[";
		for (int j = 0; j < amount; j++) {
			cout << tree[i][j] << " ";
		}
		cout << "],  ";
		while (temp % 2 == 0) {
			temp = temp / 2;
		}

		if (temp == 1) cout << "\n";
	}
}
int* sum(int* a, int* b) {
	int* res = new int[amount];
	for (int i = 0; i < amount; i++) {
		res[i] = (a[i] || b[i]);
	}

	return res;
}

int* Find(int start, int end, int left, int right, int node) {
	int f = start;
	int r = end;
	int res = 0;
	int* emp = new int[amount];
	if (start > right || end < left) { // case 1

		for (int i = 0; i < amount; i++) {
			emp[i] = 0;
		}
		return emp;
	}
	else if (start >= left && end <= right){ //case 2
		for (int i = 0; i < amount; i++) {
			emp[i] = tree[node][i];
		}
		return emp;
	}
	else // other case
	{
		int mid = (start + end) / 2;
		return sum(Find(start, mid, left, right, 2 * node) , Find(mid + 1, end, left, right, 2 * node + 1));
	}
}

bool is_possible(int left, int right,int r){
	int* pri = Find(pow2(r), pow2(r + 1) - 1, pow2(r) + left-1, pow2(r) + right-1, 1);
	bool res = 0;
	for (int i = 0; i < amount; i++) {
		//cout << pri[i] << " ";
		if (!pri[i]) return 0;
	}
	return 1;
}
int main()
{
	int n, r = 1;
	string input;
	cin >> n;

	while (pow2(r)<n) {
		r++;
	}

	int loc;
	for (int i = 0; i < n; i++) {
		cin >> input;
		if (itemnum.find(input) != itemnum.end()) {
			loc = itemnum[input];
		}
		else {
			itemnum.insert({ input, amount });
			loc = amount;
			amount++;
		}
		tree[pow2(r) + i][loc] = 1;
	}

	//트리 구성하기
	for (int i = pow2(r) - 1; i > 0; i--) {
		for (int j = 0; j < amount; j++) {
			tree[i][j] = (tree[i * 2][j] || tree[i * 2 + 1][j]);
		}
	}

	//print(r);
	int left=1, right,is_found = 0;
	for (int length = amount; length <= n;length++) {
		right = left + length - 1;
		while (right <= n) {
			if (is_possible(left, right, r)) {
				cout << left << "\n" << right;
				is_found = 1;
				break;
			}
			left++;
			right++;
		}
		if (is_found) break;
		left = 1;
	}

}
