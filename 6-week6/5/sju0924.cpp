#include <string>
#include <vector>
#include<iostream>
#include<queue>
using namespace std;

struct Process {
	int PID;
	int ExecTime;

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
	int getPID(long long k) {
		Process curP;
		bool found = false;
		long long res;
		int clear_iter,clear_PID , prev_iter=1,prev_PID = 0;

		

		while (!found) {
			if (Table.empty()) break;
			curP = Table.top();
			clear_iter = curP.ExecTime;
			clear_PID = curP.PID;
			
			curTime += (clear_iter - prev_iter) * len + (clear_PID - prev_PID);
			//cout << "iter: " << clear_iter << ", PID: " << clear_PID << ", curtime: "<<curTime<<"\n";

			
			if (curTime>= k) { //아무 프로세스도 끝나지 않았을 때
				int idx = (prev_PID + (clear_iter - prev_PID) * len + (getSerial(clear_PID) - getSerial(prev_PID))) % len;
				//cout << "idx = " << idx <<", len: "<<run.size()<<"\n";
				res = run[idx];
				found = true;
			}
			else {
				Table.pop();
				
				run.erase(run.begin()+getSerial(clear_PID));
				len--;
				if (Table.empty()) { break; }
				prev_PID = (clear_PID)%len;
				prev_iter = clear_iter;
			}
			

		}

		if (found) {
			return res;
		}
		else {
			return -1;
		}
	}
	void getTimes_io() {
		int n,  timeInput;
		long long k;
		cin >> n >> k;
		len = n;
		totallen = n;
		for (int i = 0; i < n; i++) {			
			Process pInput;
			
			cin >> timeInput;
			pInput.PID = i;
			pInput.ExecTime = timeInput;

			Table.push(pInput);
			run.push_back(i);
			remainTime.push_back(timeInput);
		}

		cout << getPID(k);
	}

	int getTimes_vec(vector<int> food_times, long long k) {
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

	int setTime(long long int time) {
		for (auto elem: run) {
			remainTime[elem] -= time;
		}
	}

};


int main() {
	RR table;
	table.getTimes_io();
}