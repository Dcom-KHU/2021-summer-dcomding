#include <cstdio>
#include <stack>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n;
map<string, vector<string> > arrivalClubs;
map<string, vector<vector<string> > > eachClubCycles;
map<string, int> clubsPtr, usedCyclePtr;
set<string> existClubs, existLastCourse;
queue<string> lastCourse;
stack<string> cycleCourse, nextClubs;
stack<pair<string, int> > funcStack, revStack;

char cDepartureClub[12], cArrivalClub[12];
string sDepartureClub, sArrivalClub;


struct compare{
    bool operator()(string& x, string& y){
        if(x.length() == y.length()) return x<y;
        else return x.length()<y.length();
    }
};

int main() {
	scanf("%d\n", &n);
	for(int cnt=0;cnt<n;++cnt){
		scanf("%s %s",cDepartureClub, cArrivalClub);
		sDepartureClub = string(cDepartureClub), sArrivalClub = string(cArrivalClub);

		if(!arrivalClubs.count(sDepartureClub)){
			arrivalClubs.insert(make_pair(sDepartureClub, vector<string>(0)));
			eachClubCycles.insert(make_pair(sDepartureClub, vector<vector<string> >()));
			clubsPtr.insert(make_pair(sDepartureClub, 0));
			usedCyclePtr.insert(make_pair(sDepartureClub, 0));
		}
		if(!arrivalClubs.count(sArrivalClub)){
			arrivalClubs.insert(make_pair(sArrivalClub, vector<string>(0)));
			eachClubCycles.insert(make_pair(sArrivalClub, vector<vector<string> >()));
			clubsPtr.insert(make_pair(sArrivalClub, 0));
			usedCyclePtr.insert(make_pair(sArrivalClub, 0));
		}
		arrivalClubs[sDepartureClub].push_back(sArrivalClub);
	}

	for(map<string,vector<string> >::iterator iter = arrivalClubs.begin(); iter != arrivalClubs.end(); ++iter)
		sort(iter->second.begin(), iter->second.end(), compare());

    for(map<string,vector<string> >::reverse_iterator iter = arrivalClubs.rbegin(); iter != arrivalClubs.rend(); ++iter)
        if(iter->first != "DCOM")
            funcStack.push(make_pair(iter->first,2));
	funcStack.push(make_pair("DCOM", 0));

	string returnClub = "";
	while(!funcStack.empty()){
		pair<string, int> status = funcStack.top(); funcStack.pop();
		string club = status.first;
		if(status.second%2==0){
			funcStack.push(make_pair(club, 1+status.second));
			existClubs.insert(club);

			if(arrivalClubs[club].size() == clubsPtr[club]){
                if(!status.second){
                    lastCourse.push(club);
                    existLastCourse.insert(club);
                }
                funcStack.pop();
                returnClub = "";
			}
			else{
				string nextClub = arrivalClubs[club][clubsPtr[club]];
				if(!existClubs.count(nextClub)){
					funcStack.push(make_pair(nextClub, status.second));
				}
				else{
					returnClub = nextClub;
				}
				++clubsPtr[club];
			}
		}
		else{
			if(returnClub == "" || returnClub == club){
				if(returnClub == club){
				    int cycleCnt = eachClubCycles[club].size();
				    eachClubCycles[club].push_back(vector<string>(0));
					while(!cycleCourse.empty()){
                        eachClubCycles[club][cycleCnt].push_back(cycleCourse.top());
						cycleCourse.pop();
					}
				}
				funcStack.push(make_pair(club, status.second-1));
			}
			else cycleCourse.push(club);
			if(existClubs.count(club))
                existClubs.erase(existClubs.find(club));
		}
	}

	while(!lastCourse.empty()){
        funcStack.push(make_pair(lastCourse.front(),0));
        lastCourse.pop();
	}

	nextClubs.push("ZZZZZZZZZZZ"); //가장 마지막 문자열
	while(!funcStack.empty()){
        pair<string, int> status = funcStack.top(); funcStack.pop();
        string club = status.first;

        printf("%s ", club.c_str());
        if(existLastCourse.count(club) && !status.second)
            existLastCourse.erase(existLastCourse.find(club));
        if(status.second == 2){
            nextClubs.pop();
            continue;
        }


        if(usedCyclePtr[club]<eachClubCycles[club].size()){
            while(usedCyclePtr[club]<eachClubCycles[club].size()){
                if(existLastCourse.count(club) && (eachClubCycles[club][usedCyclePtr[club]].size()?eachClubCycles[club][usedCyclePtr[club]][0]:club)>nextClubs.top()) break;

                for(vector<string>::iterator iter = eachClubCycles[club][usedCyclePtr[club]].begin(); iter != eachClubCycles[club][usedCyclePtr[club]].end(); ++iter)
                    revStack.push(make_pair(*iter, 1));
                revStack.push(make_pair(club, 2));
                nextClubs.push(club);

                ++usedCyclePtr[club];
            }

            while(!revStack.empty()){
                funcStack.push(revStack.top());
                revStack.pop();
            }
        }
	}

	return 0;
}
