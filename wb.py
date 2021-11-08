def findRelativeRanks(score):
    sorted_score= sorted(score, reverse=True)
    gold = sorted_score[0] 
    silver = sorted_score[1]
    bronze = sorted_score[2]
    
    placement=[]
    for i in score:
        if i== gold:
            placement.append('Gold Medal')
        elif i == silver:
            placement.append('Silver Medal')
        elif i == bronze:
            placement.append('Bronze Medal')
        else:
            if i in sorted_score:
                e= sorted_score.index(i)
                placement.append(e+1)
    print(placement)
    
    


findRelativeRanks([5,4,3,2,1])
findRelativeRanks([10,3,8,9,4])