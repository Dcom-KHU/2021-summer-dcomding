#include <iostream>
#include <bitset>
#include <cmath>
using namespace std;

bitset<15> b;
bitset<4> c;

int main(){
	int num;
	for(int i = 0; i < 15; i++){
		cin >> num;
		if(num == 1){
			b |= (1 << i);
		}
		
	}
	
	//C1
	c |= ((b[2]^b[4]^b[6]^b[8]^b[10]^b[12]^b[14]^b[0]) << 0);
	
	//C2
	c |= ((b[2]^b[5]^b[6]^b[9]^b[10]^b[13]^b[14]^b[1]) << 1);
	
	//C3
	c |= ((b[4]^b[5]^b[6]^b[11]^b[12]^b[13]^b[14]^b[3]) << 2);
	
	//C4
	c |= ((b[8]^b[9]^b[10]^b[11]^b[12]^b[13]^b[14]^b[7]) << 3);
	
	//정정
	b ^= (1 << c.to_ulong() - 1);
	
	int exp  = 0;
	int sum = 0;
	for(int i = 0; i < 15; i++){
		if(!(i == 0 || i == 1 || i == 3 || i == 7)){
			if(b[i]){
				sum += pow(2,exp);
			}
			exp++;
		}
	}
	cout << sum;
	
	//cout << b.to_ulong()
	return 0;
}

