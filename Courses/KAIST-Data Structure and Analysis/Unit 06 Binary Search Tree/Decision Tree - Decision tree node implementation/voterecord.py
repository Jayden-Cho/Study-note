class Record:

    types = ['republican','democrat']
    values = ['y','n','?']
    numValues = 16

    def __init__(self,csvline):
        self.party = csvline[0]    # 정당 추출
        self.feature = []
        for itr in range(1,len(csvline)):
            self.feature.append(csvline[itr])    # 나머지 결과물 값을 feature에 저장.

    def __str__(self):
        ret = 'Classficiation : '+self.party+', Features : '+str(self.feature)    # 출력될 때 위에서 저장된 값들 표시.
        return ret