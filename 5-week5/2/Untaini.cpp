#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int n, box;
vector<int> boxPos;

int main()
{
    scanf("%d",&n);
    for(int cnt=0; cnt<n; ++cnt){
        scanf("%d",&box);
        int curBoxPos = lower_bound(boxPos.begin(), boxPos.end(), box) - boxPos.begin();
        if(curBoxPos == boxPos.size()) boxPos.push_back(box);
        else boxPos[curBoxPos] = box;
    }
    
    printf("%d", boxPos.size());
    
    return 0;
}
