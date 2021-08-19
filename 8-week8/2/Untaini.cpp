#include <cstdio>
#define min(a,b) (a<b?a:b)

int paperCnt[5], paper[15][15], res;

int func(int pos){	
	for(int posCnt=pos;posCnt<100;++posCnt){
		int nCnt = posCnt/10, mCnt = posCnt%10;
		if(paper[nCnt][mCnt]){
			bool canPost = true;
			int lenCnt, res=99;
			for(lenCnt=1;lenCnt<5;++lenCnt){
				for(int cnt=0;cnt<=lenCnt;++cnt)
					canPost &= paper[nCnt+cnt][mCnt+lenCnt] & paper[nCnt+lenCnt][mCnt+cnt];

				if(!canPost) break;
			}

			for(int iCnt=0;iCnt<lenCnt;++iCnt)
				for(int jCnt=0;jCnt<lenCnt;++jCnt)
					paper[nCnt+iCnt][mCnt+jCnt] = 0;

			while(lenCnt--){
				if(paperCnt[lenCnt]){
					--paperCnt[lenCnt];

					int temp = func(posCnt+lenCnt+1);
					res = min(res, temp);

					++paperCnt[lenCnt];		
				}	

				for(int cnt=0;cnt<=lenCnt;++cnt)
					paper[nCnt+cnt][mCnt+lenCnt] = paper[nCnt+lenCnt][mCnt+cnt] = 1;
			}
			return res==99?res:res+1;
		}	
	}
			
	return 0;
}


int main() {
	for(int nCnt=0;nCnt<10;++nCnt)
		for(int mCnt=0;mCnt<10;++mCnt)
			scanf("%d",&paper[nCnt][mCnt]);
	
	for(int cnt=0;cnt<5;++cnt)
		paperCnt[cnt] = 5;
	
	res = func(0);
	printf("%d", res==99?-1:res);
	return 0;
}