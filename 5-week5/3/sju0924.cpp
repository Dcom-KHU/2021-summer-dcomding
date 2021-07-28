#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;

typedef pair<int, int> time;

class computers {
private:
	int ea;
	vector<vector<time>> timetable;
public:
	computers() {
		ea = 0;
		vector<time>input; 
		input.push_back(make_pair(0, 1000001));
		timetable.push_back(input);
	}

	//입력: 컴퓨터 번호, 시작/끝 시간
	//출력: 빈 컴퓨터를 찾았는지 여부
	int getEmpty(int computer, time _t) {
		int found = 0;
		int temp;
		//cout << timetable[computer].size()<<;
		
		for (int i = 0; i < timetable[computer].size();i++) {
			time cur = timetable[computer][i];
			if (cur.first > _t.second) break;
			if (_t.first >= cur.first && _t.second <= cur.second) { //찾았을 시
				time cur = timetable[computer][i];
				temp = cur.second;
				timetable[computer][i].second = _t.first;
				timetable[computer].push_back(make_pair(_t.second, temp));
				

				if (i != timetable[computer].size() - 2) {
					swap(timetable[computer][i + 1], timetable[computer][timetable[computer].size() - 1]);
				}

				found = 1;

			}
		}
		//printTimeTable();
		return found;
	}

	//입력: 유저의 사용시간
	//출력: 유저가 사용하는 컴퓨터
	int addUser(time _t) {
		int computer= 0;
		while (!getEmpty(computer,_t)) {
			
			computer++;
			if (computer > ea) {
				ea++;
				vector<time> input;
				input.push_back(make_pair(0, _t.first));
				input.push_back(make_pair(_t.second, 1000001));
				timetable.push_back(input);
				break;
			}
		}

		return computer;
	}
	void swap(time& a, time& b) {
		time temp;
		temp = a;
		a = b;
		b = temp;
	}
	int getEA() {
		return ea+1;
	}

	void printTimeTable() {
		for (int i = 0; i < timetable.size();i++) {
			for (int j = 0; j < timetable[i].size();j++) {
				cout << "("<<timetable[i][j].first << " " << timetable[i][j].second << "), ";
			}
			cout << "\n";
		}
	}
};
int res[100001];

int main() {

	
	int n, start, end, cp;
	vector<time> Users;
	computers XZ_Room;
	
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> start >> end;
		Users.push_back(make_pair(start, end));

	}

	sort(Users.begin(), Users.end());
		
	
	for (int i = 0; i < n; i++) {
		start = Users[i].first;
		end = Users[i].second;
		cp = XZ_Room.addUser(make_pair(start, end));
		res[cp]++;
	}

	cout << XZ_Room.getEA()  << "\n";
	for (int i = 0; i < XZ_Room.getEA();i++) {
		cout << res[i] << " ";
	}
}