//시뮬레이션 문제
/*
sum 값을 계속 들고갈 수 없다.
평균 필터 알고리즘 사용할 것.
*/
#include <iostream>
#include <vector>
using namespace std;
vector<int> blocks;

int sample_num = 0;
double prev_avg = 0;
double avg_filter(double x){
	double avg, a;
	sample_num++;
	a = (sample_num - 1)/ (sample_num + 0.0);
	avg = a * prev_avg + (1 - a) * x;
	prev_avg = avg;
	return avg;
}


int main(){
	int n, m;
	cin >> n >> m;
	bool flag = true;
	for(int i = 0; i < n; i++){
		int num;
		cin >> num;
		blocks.push_back(num);
	}
	
	for(int i = 1; i < n; i++){
		int block =  blocks[n-i];
		int pre_block = blocks[n-i-1];
		prev_avg = avg_filter(block);
		int start = pre_block - m;
		int end = pre_block + m;
		if(prev_avg <= start || prev_avg >= end){
			flag = false;
			break;
		}
	}
	
	if(flag){
		cout << 1;
	}else{
		cout << 0;
	}
	return 0;
	
}