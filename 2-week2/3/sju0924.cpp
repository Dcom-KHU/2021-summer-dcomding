#include <iostream>
#include<stack>
#include<string>
#include<vector>

using namespace std;

string club[5001];
string res[5001];
vector<vector<pair<int,int>>> tree(5001);
stack<int>st;

int get_number(string _c, int size);
int search(int cur,int cnt);
int N;
int main()
{
	int cnt=0,nf,nt,Size = 0;
	string from,to;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> from>>to;
		
		nf = get_number(from, Size);
		if (nf == -1) {
			club[Size] = from;
			nf =Size;
			Size++;
		}

		nt = get_number(to, Size); 
		if (nt == -1) {
			club[Size] = to;
			nt = Size;
			Size++;
		}
		tree[nf].push_back(make_pair(nt,0));
		
	}

	int temp;
	int start;

	//이름순 내림차순으로 정렬하기
	for (int i = 0; i < Size;i++) {
		if (club[i] == "DCOM") start = i;
		for (int j = 0; j < tree[i].size();j++) {
			for (int k = j + 1; k < tree[i].size();k++) {
				if (club[tree[i][j].first] > club[tree[i][k].first]) {//이름 빠른게 앞으로 가야 함
					temp = tree[i][j].first;
					tree[i][j].first = tree[i][k].first;
					tree[i][k].first = temp;
				}
			}
		}
	}
	search(start, 0);
	for (int i = 0; i <= N; i++) {
		cout << res[i] << " ";
	}

}

int get_number(string _c, int size) {
	int cnt = 0;
	while (club[cnt] != _c && cnt < size) {
		cnt++;
	}

	if (cnt == size) return -1;
	return cnt;
}
int search(int cur,int cnt) {
	bool is_searched=false, is_left = false;

	if (cnt == N) {
		res[N] = club[cur];
		return true;
	}
	else if (cnt == N) {
		return false;
	}

	res[cnt] = club[cur];
	for (int i = 0;i < tree[cur].size();i++) {
		if (tree[cur][i].second) continue;
		is_left = true;
		//res[cnt] = club[tree[cur][i].first];
		tree[cur][i].second = 1;
		is_searched = search(tree[cur][i].first, cnt + 1);
		if (is_searched) return true;

		tree[cur][i].second = 0;
	}


	return false;
}