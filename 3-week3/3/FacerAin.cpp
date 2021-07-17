#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

deque<int> bus;
deque<int> student;
//hh mm => m
int convert_to_min(int h, int m){
	return (h*60 + m);
}
void print_to_hour(int m){
	cout << m/60 << " " << m%60 << endl;
}
int main(){
	int n,t,m,k;
	cin >> n >> t >> m >> k;
	for(int i = 0; i < k; i++){//학생 입력
		int h, m;
		cin >> h >> m;
		student.push_back(convert_to_min(h, m));
	}
	sort(student.begin(), student.end());
	
	int time_num = 0;
	for(int i = 0; i < n; i++){
		bus.push_back(540+time_num);
		time_num += t;
	}
	
	int last_bus = bus.back();
	int last_student;
	int p_num = 0;
	while(!student.empty()){

		p_num++;
		last_student = student.front();
		student.pop_front();
		
		if(p_num == m || student.front() > bus.front()){
			bus.pop_front();
			if(bus.empty()){
				break;
			}
			p_num = 0;
		}
		
	}
	if(!bus.empty() && student.empty()){
		print_to_hour(last_bus);
	}else{
		
		if((p_num == m) && last_student <= last_bus){
			
			print_to_hour(last_student-1);
		}else{
			print_to_hour(last_bus);
		}
	}
	
	return 0;
	
		  
}
