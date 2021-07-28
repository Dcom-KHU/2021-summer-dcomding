#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;

#define pii pair<int,int>

int n, st, ed, segTree[1<<22], ptr=1<<21;
vector<pii> timetable;
vector<int> computers, endTimes;
map<int,priority_queue<int>> timeComputer;

void update(int num, int val){
    segTree[num+=ptr] = val;
    while(num>>=1)
        segTree[num] = min(segTree[num*2], segTree[num*2+1]);
}

int getMin(int st, int ed){
    st+=ptr, ed+=ptr;
    int res = 1000001;
    while(st<=ed){
        if(st%2==1) res = min(res, segTree[st]), ++st;
        if(ed%2==0) res = min(res, segTree[ed]), --ed;
        st>>=1, ed>>=1;
    }
    return res;
}

int main()
{
    scanf("%d",&n);
    for(int cnt=0; cnt<n; ++cnt){
        scanf("%d%d",&st,&ed);
        timetable.push_back(make_pair(st,ed));
    }
    
    sort(timetable.begin(), timetable.end());
    fill(segTree, segTree+ptr*2, 1000001);
    
    for(auto iter = timetable.begin(); iter != timetable.end(); ++iter){
        int minPos = getMin(0, iter->first);
        if(!timeComputer.count(iter->second))
            timeComputer.insert(make_pair(iter->second, priority_queue<int>()));
        
        if(minPos == 1000001){
            timeComputer[iter->second].push(-computers.size());
            if(timeComputer[iter->second].top() == -computers.size())
                update(iter->second, computers.size());
            
            computers.push_back(1);
            endTimes.push_back(iter->second);
        }
        else{
            ++computers[minPos];
            timeComputer[endTimes[minPos]].pop();
            
            if(timeComputer[endTimes[minPos]].size())
                update(endTimes[minPos], timeComputer[endTimes[minPos]].top());
            else
                update(endTimes[minPos], 1000001);
            
            timeComputer[endTimes[minPos]=iter->second].push(-minPos);
            if(timeComputer[iter->second].top() == -minPos)
                update(iter->second, minPos);
        }
    }
    
    printf("%d\n", computers.size());
    for(auto iter = computers.begin(); iter != computers.end(); ++iter)
        printf("%d ", *iter);
        
    return 0;
}
