#include <cstdio>
#include <vector>
#include <stack>
#include <map>
#include <string>
#include <queue>
using namespace std;

int n;
map<string, priority_queue <string, vector<string>, greater<string> > > tickets;
stack<string> resultStack, funcStack;
char cDepartureClub[12], cArrivalClub[12];
string sDepartureClub, sArrivalClub;


int main() {
	scanf("%d\n", &n);
	for(int cnt=0;cnt<n;++cnt){
		scanf("%s %s",cDepartureClub, cArrivalClub);
		sDepartureClub = string(cDepartureClub), sArrivalClub = string(cArrivalClub);

		if(!tickets.count(sDepartureClub))
            tickets.insert(make_pair(sDepartureClub, priority_queue<string, vector<string>, greater<string> >()));
		if(!tickets.count(sArrivalClub))
            tickets.insert(make_pair(sArrivalClub, priority_queue<string, vector<string>, greater<string> >()));

        tickets[sDepartureClub].push(sArrivalClub);
	}

	funcStack.push("DCOM");
	while(!funcStack.empty()){
        string club = funcStack.top();
        if(tickets[club].empty()){
            resultStack.push(club);
            funcStack.pop();
        }
        else{
            funcStack.push(tickets[club].top());
            tickets[club].pop();
        }
	}

	while(!resultStack.empty()){
        printf("%s ",resultStack.top().c_str());
        resultStack.pop();
	}

    return 0;
}
