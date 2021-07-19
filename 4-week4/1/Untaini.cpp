#include <cstdio>
#include <stack>
using namespace std;

int n, k, machine[101][101], height[101], actions[101], result;
stack<int> basket;

int main()
{
    scanf("%d%d", &n, &k);
    
    for(int aCnt=0; aCnt<k; ++aCnt)
        scanf("%d", &actions[aCnt]);
        
    for(int col=n; col>0; --col)
        for(int row=1; row<=n; ++row){
            scanf("%d", &machine[row][col]);
            if(machine[row][col] && !height[row])
                height[row] = col;
        }
        
    for(int aCnt=0; aCnt<k; ++aCnt){
        int row = actions[aCnt], col = height[row], doll = machine[row][col];
        
        if(col){
            --height[row];
            if(!basket.empty() && basket.top() == doll){
                result+=2;
                basket.pop();
            }
            else
                basket.push(doll);
        }
    }
    
    printf("%d", result);
    return 0;
}
