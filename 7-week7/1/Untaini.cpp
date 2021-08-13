#include <cstdio>
#include <stack>
using namespace std;

int n, bCnt;
double sum, avg, m, block;
stack<double> blocks;
int main()
{
    scanf("%d%lf",&n,&m);
    for(int cnt=0; cnt<n; ++cnt){
        scanf("%lf",&block);
		//무게중심은 현재 블록보다 위에 있는 블록들의 무게중심의 평균이니
		//stack을 이용해서 맨 위부터 계산하게 함
        blocks.push(block);
    }
	
	//맨 위에 있는 블록의 중심점을 저장하고 스택에서 제외함
	sum=avg=blocks.top(), ++bCnt;
    blocks.pop();
	
	//젠가가 무너졌는지 확인하기 위함
    bool isFallen = false;
    
    while(!blocks.empty() && !isFallen){
        block = blocks.top(); blocks.pop();
		
		//무게 중심의 평균이 블록을 넘어선다면 isFallen이 false가 됨
		//즉, 한번이라도 무너진다면 while문을 탈출함
        isFallen = block-m >= avg || avg >= block+m;
        avg = (sum+=block)/++bCnt;
    }
    
	//무너짐 여부를 출력함
    printf("%d", !isFallen);
    return 0;
}
