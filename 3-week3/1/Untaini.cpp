#include <cstdio>

int n,k,book,existBook[200001],bookCnt;
vector<int> bookList;

int main() {
	scanf("%d%d",&n,&k);
	for(int cnt=0;cnt<n;++cnt){
		scanf("%d",&book);
		if(!existBook[book])
			++existBook[book], ++bookCnt;
	}
	
	printf("%d",bookCnt<k?bookCnt:k);
	return 0;
}