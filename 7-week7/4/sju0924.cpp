#include<iostream>
#include<string>
#include<map>
#include<vector>

using namespace std;
string input;
int result;
int arr[20001];
map<char, vector<string>> piece;

int Min(int a, int b) {
	if (a < b) return a;
	else return b;
}
int getLength(int cur) {
	int res = input.length() + 1;
	if (arr[cur]) return arr[cur];
	if (cur >= input.length()) {
		return 0;
	}
	char curChar = input[cur];
	int itemlen;
	for (auto item : piece[curChar]) {
		itemlen = item.size();
		if (item == input.substr(cur,itemlen)) {
			res = Min(res, getLength(cur + itemlen) + 1);
		}
	}
	arr[cur] = res;
	return res;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	int n;
	string pic;
	
	cin >>n;
	cin >> input;
	for (int i = 0; i < n; i++) {
		cin >> pic;
		if (piece.find(pic[0]) == piece.end()) {
			vector<string> newvec;
			piece.insert(make_pair(pic[0], newvec));
		}
		piece[pic[0]].push_back(pic);
		
	}

	result = getLength(0);
	if (result == input.size() + 1) {
		cout << -1 << "\n";
	}
	else {
		cout << result << "\n";
	}

}