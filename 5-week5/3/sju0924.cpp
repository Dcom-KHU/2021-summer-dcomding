#include <iostream>
#include <queue>
#include<algorithm>
#include<vector>
using namespace std;

typedef pair<int, int> tme; // 종료 시간, 컴퓨터 번호

int res[100001];
void printpq(priority_queue<tme, vector<tme>, greater<tme>> pq) {
	priority_queue<tme,vector<tme>, greater<tme>> tmp = pq;
	vector<tme> vtmp;
	for (int i = 0; i < pq.size();i++) {
		vtmp.push_back(tmp.top());
		tmp.pop();
	}
	for (int i = vtmp.size() - 1; i >= 0;i--) {
		cout << "(" << vtmp[i].first << " " << vtmp[i].second << ") ,";
	}
	cout << "\n";
}

int main() {

	
	priority_queue< int, vector<int>, greater<int>> freeCom;
	priority_queue<tme, vector<tme>, greater<tme>> OccupiedCom;
	vector<tme>Users;
	int comNum = 0;

	int n,start,end;
	
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> start >> end;
		Users.push_back(make_pair(start, end));

	}

	sort(Users.begin(), Users.end());
		
	
	int newlyUsedCom;
	tme User;
	for (int i = 0; i < n; i++) {
		User = Users[i];
		
		//printpq(OccupiedCom);
		if(OccupiedCom.size())
			//cout << "next available Computer: " << OccupiedCom.top().first << ", next User start time " << User.first << "\n";
		while (!OccupiedCom.empty() && OccupiedCom.top().first<=User.first) {
			//cout << "freed " << OccupiedCom.top().second << "\n";
			freeCom.push(OccupiedCom.top().second);
			OccupiedCom.pop();
		}

		if (!freeCom.size()) {
			freeCom.push(comNum);
			comNum++;
		}

		newlyUsedCom = freeCom.top();
		res[newlyUsedCom]++;
		freeCom.pop();

		
		//cout << "User end time: " << User.second << ", his computer: " << newlyUsedCom << "\n";
		OccupiedCom.push(make_pair(User.second, newlyUsedCom));

		//cout << i << " " << freeCom.size() << "\n";


	}

	cout << comNum << "\n";
	for (int i = 0; i < comNum;i++) {
		cout << res[i] << " ";
	}
}