'''
多次元配列の各項目をkeyにしてsortしたい場合、operator.itemgetterを使って
Slice範囲を指定するとやりやすい。

# 参考
https://qiita.com/t_kanno/items/13dd226e70d080159d97
'''

''' e,g,
from operator import itemgetter

temp = [[[None] * 10 for _ in range(10)] for _ in range(10)]
temp.sort(key=itemgetter(slice(0, 9)))
'''

'''
下記の問題では、
[[-5, 0, 0, 'A'], [0, -2, -3, 'B'], [0, -3, -2, 'C']]
を
[[-5, 0, 0, 'A'], [0, -3, -2, 'C'], [0, -2, -3, 'B']]
のようにソートしている。
数字に負の符号がついているのは、数字は降順でソートしたいが、最後の文字列は昇順でソートしたいため。
'''

# https://leetcode.com/contest/weekly-contest-178/problems/rank-teams-by-votes/

from operator import itemgetter
class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        if votes is None or len(votes) == 0:
            return None

        l = len(votes[0])
        # rankMap = [[0] * l for _ in range(l)]
        rankMap = {}
        p = l + 1
        ans = []

        for i in range(len(votes)):
            vote = votes[i]

            for j in range(len(vote)):
                # rank = j + 1
                rank = j
                team = vote[j]
                if team not in rankMap:
                    rankMap[team] = [0]*l
                    # rankMap[team][rank] += 1
                    rankMap[team][rank] -= 1
                else:
                    # rankMap[team][rank] += 1
                    rankMap[team][rank] -= 1


        for key, val in rankMap.items():
            ans.append(val + [key])

        print(rankMap)
        print(ans)

        ans.sort(key=itemgetter(slice(0, l+1)))
        # ans.sort(key=itemgetter(slice(0, l)), reverse=True)

        print(ans)
        temp = ''
        for i in range(len(ans)):
            temp += ans[i][l]

        return temp



votes = ["ABC","ACB","ABC","ACB","ACB"]
# votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
# votes = ["WXYZ","XYZW"]
# votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
# votes = ["M","M","M","M"]
# votes = ["FVSHJIEMNGYPTQOURLWCZKAX","AITFQORCEHPVJMXGKSLNZWUY","OTERVXFZUMHNIYSCQAWGPKJL","VMSERIJYLZNWCPQTOKFUHAXG","VNHOZWKQCEFYPSGLAMXJIUTR","ANPHQIJMXCWOSKTYGULFVERZ","RFYUXJEWCKQOMGATHZVILNSP","SCPYUMQJTVEXKRNLIOWGHAFZ","VIKTSJCEYQGLOMPZWAHFXURN","SVJICLXKHQZTFWNPYRGMEUAO","JRCTHYKIGSXPOZLUQAVNEWFM","NGMSWJITREHFZVQCUKXYAPOL","WUXJOQKGNSYLHEZAFIPMRCVT","PKYQIOLXFCRGHZNAMJVUTWES","FERSGNMJVZXWAYLIKCPUQHTO","HPLRIUQMTSGYJVAXWNOCZEKF","JUVWPTEGCOFYSKXNRMHQALIZ","MWPIAZCNSLEYRTHFKQXUOVGJ","EZXLUNFVCMORSIWKTYHJAQPG","HRQNLTKJFIEGMCSXAZPYOVUW","LOHXVYGWRIJMCPSQENUAKTZF","XKUTWPRGHOAQFLVYMJSNEIZC","WTCRQMVKPHOSLGAXZUEFYNJI"]
print(Solution().rankTeams(votes))