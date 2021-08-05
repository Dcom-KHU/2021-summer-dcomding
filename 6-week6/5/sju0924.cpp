#include <string>
#include <vector>
#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;

struct Process {
	int PID;
	long long int ExecTime;

	bool operator<(Process _other) const {

		if (this->ExecTime == _other.ExecTime) {
			return this->PID > _other.PID;
		}
		else return this->ExecTime > _other.ExecTime;
		
	}
};
class RR {
private:
	priority_queue<Process> Table;
	vector<int>run;
	vector<int>remainTime;
	long long curTime=0;
	int totallen;
	int len;

public:

	long long int getPID(long long k) {
		Process curP;
		bool found = false;
		long long res;
		long long int clear_iter, prev_iter = 0;
		while (true) {
			curP = Table.top();
			clear_iter = curP.ExecTime;

			if (curTime + (clear_iter - prev_iter) * len > k)
				break;
			else curTime += (clear_iter - prev_iter) * len;
			Table.pop();
			len--;

			prev_iter = clear_iter;

		}
		vector<int>remain;
		while (!Table.empty()) {
			curP = Table.top();
			Table.pop();
			remain.push_back(curP.PID);

		}

		sort(remain.begin(), remain.end());
		res = remain[(k - curTime) % remain.size()];
		return res;

	}
	void getTimes_io() {
		int n,  timeInput;
		long long k,sum = 0;
		cin >> n >> k;
		len = n;
		totallen = n;
		for (int i = 0; i < n; i++) {			
			Process pInput;
			
			cin >> timeInput;
			pInput.PID = i;
			pInput.ExecTime = timeInput;
			sum += timeInput;

			Table.push(pInput);
			run.push_back(i);
			remainTime.push_back(timeInput);
		}
		if (sum <= k) {
			cout << -1;
		}
		else
			cout << getPID(k);
	}

};


int main() {
	RR table;
	table.getTimes_io();
}