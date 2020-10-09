import itertools


class qualify_permutations:
    def __init__ (self,table,matches,pointsOnVictory=2):
        self.table=table
        self.matches=matches
        self.pointsOnVictory=pointsOnVictory

    def calculate_qualification_possiblity(self,team,lastSpotAtWhichQualificationOccurs=4,numberOfMatchesToPredict=20):

        res = ["".join(seq) for seq in itertools.product("01", repeat=numberOfMatchesToPredict)]
        qualify=[]
        ans=0

        for x in res:
            temp_table=self.table.copy()
            for i in range(numberOfMatchesToPredict):
                if x[i]=='0':
                    temp_table[self.matches[i][0]]+=self.pointsOnVictory
                else:
                    temp_table[self.matches[i][1]]+=self.pointsOnVictory

            points=[temp_table[i] for i in temp_table]
            points.sort(reverse = True)

            if temp_table[team]>points[4]:
                ans+=1
                qualify.append(x)
        
        return ans,qualify

    def canCompress(self,a,b,l):
        count=0
        index=-1
        for i in range(l):
            if a[i]!=b[i]:
                count=count+1
                index=i
        if count==1:
            return index
        return -1

    def compress(self,qualify,numberOfMatchesToPredict=20):
        l=numberOfMatchesToPredict
        final=[]
        
        num=len(qualify)
        while num>0:
            newQualify=[]
            mark=[]
            for i in range(num):
                mark.append(0)
            
            for i in range(num):
                if mark[i]:
                    continue
                for j in range(i+1,num):
                    if mark[j]:
                        continue
                    index=self.canCompress(qualify[i],qualify[j],l)        
                    if index>=0:
                        mark[i]=1
                        mark[j]=1
                        newQualify.append(qualify[i][0:index]+'-'+qualify[i][index+1:l])
                        break
                if mark[i]!=1:
                    final.append(qualify[i])
                
            qualify=newQualify.copy()
            num=len(qualify)
            print(num)

        return final



# contains the current points table of the tournament
# let us assume that n matches are left in tournament
table={
    'mi':14,
    'dc':12,
    'srh':12,
    'rcb':10,
    'rr':8,
    'kkr':6,
    'csk':6,
    'kxip':4,
}

# contains the list of the next n matches in the tournament in reverse order
# mi vs srh is the last match
# dc vs rcb is the second last match and so on.....
matches=[
    ['mi','srh'],
    ['dc','rcb'],
    ['kkr','rr'],
    ['csk','kxip'],
    ['rcb','srh'],
    ['dc','mi'],
    ['kxip','rr'],
    ['csk','kkr'],
    ['mi','rcb'],
    ['srh','dc'],
    ['kkr','kxip'],
    ['rr','mi'],
    ['rcb','csk'],
    ['kxip','srh'],
    ['kkr','dc'],
    ['csk','mi'],
    ['rr','srh'],
    ['kkr','rcb'],
    ['kxip','dc'],
    ['csk','rr']
]
# third argument in the number of points a team get on victory
tournament=qualify_permutations(table,matches,2)

# lastSpotAtWhichQualificationOccurs is the argument which tell that at which spot qualification occurs 
# for example in ipl qualification occurs at 4th spot and above
# numberOfMatchesToPredict has to be equal to n (number of matches left in the tournament)
ans,qualify=tournament.calculate_qualification_possiblity(team='kxip',lastSpotAtWhichQualificationOccurs=4,numberOfMatchesToPredict=20)

qualify=tournament.compress(qualify)
print(len(qualify))





































# final=[]
# mark=[]
# for i in range(len(qualify)):
# 	mark.append(0)
# for i in range(len(qualify)):
#     for j in range(len(qualify)):
#         if qualify[i]!=qualify[j] and mark[i]==0 and mark[j]==0:
#             k=check(qualify[i],qualify[j])
#             if k>=0:
#                 final.append(qualify[i][0:k]+"-"+qualify[i][k+1:13])
#                 mark[i]=1
#                 mark[j]=1
#                 break
# mark=[]
# qualify=final
# final=[]
# for i in range(len(qualify)):
# 	mark.append(0)
# for i in range(len(qualify)):
#     for j in range(len(qualify)):
#         if qualify[i]!=qualify[j] and mark[i]==0 and mark[j]==0:
#             k=check(qualify[i],qualify[j])
#             if k>=0:
#                 final.append(qualify[i][0:k]+"-"+qualify[i][k+1:13])
#                 mark[i]=1
#                 mark[j]=1
#                 break
# mark=[]
# qualify=final
# final=[]
# for i in range(len(qualify)):
# 	mark.append(0)
# for i in range(len(qualify)):
#     for j in range(len(qualify)):
#         if qualify[i]!=qualify[j] and mark[i]==0 and mark[j]==0:
#             k=check(qualify[i],qualify[j])
#             if k>=0:
#                 final.append(qualify[i][0:k]+"-"+qualify[i][k+1:13])
#                 mark[i]=1
#                 mark[j]=1
#                 break
# mark=[]
# qualify=final
# final=[]
# for i in range(len(qualify)):
# 	mark.append(0)
# for i in range(len(qualify)):
#     for j in range(len(qualify)):
#         if qualify[i]!=qualify[j] and mark[i]==0 and mark[j]==0:
#             k=check(qualify[i],qualify[j])
#             if k>=0:
#                 final.append(qualify[i][0:k]+"-"+qualify[i][k+1:13])
#                 mark[i]=1
#                 mark[j]=1
#                 break
# mark=[]
# qualify=final
# final=[]
# for i in range(len(qualify)):
# 	mark.append(0)
# for i in range(len(qualify)):
#     for j in range(len(qualify)):
#         if qualify[i]!=qualify[j] and mark[i]==0 and mark[j]==0:
#             k=check(qualify[i],qualify[j])
#             if k>=0:
#                 final.append(qualify[i][0:k]+"-"+qualify[i][k+1:13])
#                 mark[i]=1
#                 mark[j]=1
#                 break
# mark=[]
# qualify=final
# final=[]
# for i in range(len(qualify)):
# 	mark.append(0)
# for i in range(len(qualify)):
#     for j in range(len(qualify)):
#         if qualify[i]!=qualify[j] and mark[i]==0 and mark[j]==0:
#             k=check(qualify[i],qualify[j])
#             if k>=0:
#                 final.append(qualify[i][0:k]+"-"+qualify[i][k+1:13])
#                 mark[i]=1
#                 mark[j]=1
#                 break
# mark=[]
# qualify=final
# final=[]
# for i in range(len(qualify)):
# 	mark.append(0)
# for i in range(len(qualify)):
#     for j in range(len(qualify)):
#         if qualify[i]!=qualify[j] and mark[i]==0 and mark[j]==0:
#             k=check(qualify[i],qualify[j])
#             if k>=0:
#                 final.append(qualify[i][0:k]+"-"+qualify[i][k+1:13])
#                 mark[i]=1
#                 mark[j]=1
#                 break
# mark=[]
# qualify=final
# final=[]
# for i in range(len(qualify)):
# 	mark.append(0)
# for i in range(len(qualify)):
#     for j in range(len(qualify)):
#         if qualify[i]!=qualify[j] and mark[i]==0 and mark[j]==0:
#             k=check(qualify[i],qualify[j])
#             if k>=0:
#                 final.append(qualify[i][0:k]+"-"+qualify[i][k+1:13])
#                 mark[i]=1
#                 mark[j]=1
#                 break
# mark=[]
# qualify=final
# final=[]
# for i in range(len(qualify)):
# 	mark.append(0)
# for i in range(len(qualify)):
#     for j in range(len(qualify)):
#         if qualify[i]!=qualify[j] and mark[i]==0 and mark[j]==0:
#             k=check(qualify[i],qualify[j])
#             if k>=0:
#                 final.append(qualify[i][0:k]+"-"+qualify[i][k+1:13])
#                 mark[i]=1
#                 mark[j]=1
#                 break

# print(len(final))
# final = list(dict.fromkeys(final))                        
# print(final)