gems=[]
for i in range(int(input())):
    gems.append(str(input()))
def solution(gems):
    TYPE_NUM=len(set(gems))
    GEM_NUM=len(gems)
    cur_shop={gems[0]:1}
    cand=[]
    l_idx,r_idx=0,0
    DIST,RESULT=0,1
    
    while l_idx<GEM_NUM and r_idx<GEM_NUM:
        if len(cur_shop)<TYPE_NUM:
            r_idx+=1
            if r_idx==GEM_NUM:
                break
            cur_shop[gems[r_idx]]=cur_shop.get(gems[r_idx],0)+1
            
        else:
            cand.append((r_idx-l_idx,[l_idx+1,r_idx+1]))
            cur_shop[gems[l_idx]]-=1
            if cur_shop[gems[l_idx]]==0:
                del cur_shop[gems[l_idx]]
            l_idx+=1
    cand=sorted(cand,key=lambda x:(x[DIST],x[RESULT]))
    print(cand[0][RESULT][0])
    return cand[0][RESULT][1]
solution(gems)
#print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
#투포인터 알고리즘 사용
#두 포인터를 설정하여 4가지 보석이 존재하지 않으면 end를 증가시키고 4가지 보석이 존재하면 start를 증가시킴