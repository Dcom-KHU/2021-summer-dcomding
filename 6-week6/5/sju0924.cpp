#include <string>
#include <vector>
#include<iostream>
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

	int getSerial(int n) { //n이 실행 중인 몇 번째 프로세스인지 찾음
		int res = -1;
		int front=0, rear=len-1,mid;	

		while (front <= rear) {
			
			mid = (front + rear) / 2;
			//cout << front << " " << rear << "\n";
			//cout << "run[mid] = " << run[mid] << "\n";
			if (run[mid] < n) {
				front = mid + 1;
			}
			else if (run[mid] > n) {
				rear = mid - 1;
			}
			else if (run[mid] == n) {
				res = mid;
				break;
			}

		}

		return res;
	}
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
		//cout<< remain.size()<<"\n";
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

	long long int getTimes_vec(vector<int> food_times, long long k) {
		len = food_times.size();
		totallen = len;
		for (int i = 0; i < food_times.size(); i++) {
			Process pInput;

	
			pInput.PID = i;
			pInput.ExecTime = food_times[i-1];

			Table.push(pInput);
			run.push_back(i);
			remainTime.push_back(food_times[i-1]);
		}
		return getPID(k);
	}

	int setTime(long long int time,int PID) {
		for (auto elem: run) {
			remainTime[elem] -= time;
			if (elem < PID) remainTime[elem]++;
		}
	}

};


int main() {
	RR table;
	table.getTimes_io();
}