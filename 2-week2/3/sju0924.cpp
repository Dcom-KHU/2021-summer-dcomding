#include <iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

struct ticket {
	string first;
	string second;

	const bool operator<(ticket& other) {
		if (this->second.size() < other.second.size()) {
			return true;
		}
		else if (this->second.size() == other.second.size() && this->second < other.second) {
			return true;
		}
		else return false;
	}

	
};
ticket tickets[100001];
bool visit[100001];
string res [100001];


int search(string cur,int cnt);
int N;
int main()
{
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int cnt=0,nf,nt,Size = 0;
	string from,to;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> from>>to;		
		tickets[i].first = from;
		tickets[i].second = to;
	}
	sort(tickets, tickets + N);

	int temp;
	int start;

	
	search("DCOM", 0);
	for (int i = 0; i <= N; i++) {
		cout << res[i] << " ";
	}

}
int search(string cur,int cnt) {
	bool is_searched=false, is_left = false;
	if (cnt == N) {
		res[cnt] = cur;
		return true;
	}
	for (int i = 0;i <N;i++) {
		if (visit[i] == false and cur == tickets[i].first) {
			visit[i] = true;
			is_searched = search(tickets[i].second, cnt + 1);
			if (is_searched) {
				res[cnt] = cur;			
				return true;
			}
			visit[i] = false;
		}
	}


	return false;
}