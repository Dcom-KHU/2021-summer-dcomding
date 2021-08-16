#include <cstdio>

int paper[10][10], usedPaper[10][10], res;
bool allCanPost=true;
int main() {
	for(int nCnt=0;nCnt<10;++nCnt)
		for(int mCnt=0;mCnt<10;++mCnt)
			scanf("%d",&paper[nCnt][mCnt]);
	
	
	for(int paperSize=5; paperSize>0; --paperSize){
		int paperCnt=0;
		
		for(int nCnt=0;nCnt<10;++nCnt)
			for(int mCnt=0;mCnt<10;++mCnt)
				if(paper[nCnt][mCnt]){
					if(nCnt+paperSize>10 || mCnt+paperSize>10)
						continue;
					
					bool canPost = true;
					for(int iCnt=nCnt; iCnt<nCnt+paperSize; ++iCnt)
						for(int jCnt=mCnt; jCnt<mCnt+paperSize; ++jCnt)
							canPost &= paper[iCnt][jCnt] && !usedPaper[iCnt][jCnt];
					
					if(canPost){
						++res, ++paperCnt;
						for(int iCnt=nCnt; iCnt<nCnt+paperSize; ++iCnt)
							for(int jCnt=mCnt; jCnt<mCnt+paperSize; ++jCnt)
								++usedPaper[iCnt][jCnt];
					}
				}
		
		allCanPost &= paperCnt<=5;
	}
	printf("%d",allCanPost?res:-1);
	return 0;
}