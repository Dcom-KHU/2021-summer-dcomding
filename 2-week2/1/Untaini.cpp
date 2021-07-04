#include <cstdio>

int bit[16], errorBit, parityBit, pBitPos; //결과는 사용하지 않은 bit[0]에 저장

int main() {
	for(int cnt=1;cnt<16;++cnt)
		scanf("%d",&bit[cnt]);
	
	for(int cnt=0;cnt<4;++cnt){
		pBitPos = (1<<cnt);
		parityBit = bit[pBitPos];
		
		for(int bitCheckCnt = pBitPos+1; bitCheckCnt<16; ++bitCheckCnt)
			if((bitCheckCnt/pBitPos)%2==1)
				parityBit ^= bit[bitCheckCnt];
			
		if(parityBit)
			errorBit+=pBitPos;
	}
	
	if(errorBit)
		bit[errorBit]^=1;
	
	for(int bitCnt=1,pow=0;bitCnt<16;++bitCnt)
		if((bitCnt&-bitCnt)!=bitCnt)
			bit[0] += bit[bitCnt]<<pow++;
	
	printf("%d",bit[0]);
	return 0;
}