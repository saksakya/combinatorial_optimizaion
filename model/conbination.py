import math
import pulp as pp

class find_combination(object):
    def __init__(self, nl, status, max_member, min_member):
        self.number_list = nl
        self.status = status
        self.n = len(nl)
        self.max_member = max_member
        self.min_member = min_member
        # 最低限必要なグループ数
        self.group_nums = math.ceil((status == True).sum() / max_member)
        # グループリスト作成
        self.group_list = [self.num_to_alpha(g + 1) for g in range(self.group_nums)]
        # 個人とグループの全組み合わせ
        self.pariticipant_group = [(i,g) for i, s in enumerate(self.status) for g in self.group_list]
        # 個人と個人の全組み合わせ
        self.pair= [(i,j) for i, s in enumerate(self.status) for j, k in enumerate(self.status)]
        # print(self.pariticipant_group)
        
    def num_to_alpha(self, num):
        """数値→アルファベット変換"""
        if num <= 26:
            return chr(64 + num)
        elif num % 26 == 0:
            return self.num_to_alpha(num // 26 - 1) + chr(90)
        else:
            return self.num_to_alpha(num // 26) + chr(64 + num % 26)

    def calc(self):
        problem = pp.LpProblem('combination',pp.LpMinimize)

        # 変数の定義 (Memo binary:0or1)
        x = pp.LpVariable.dicts('x', self.pariticipant_group, cat = 'Binary')
        y = pp.LpVariable.dicts('y', self.pair, cat = 'Binary')

        #print(x)
        #print(y)
        
        # 目的条件(回数の総和ができる限り少なくなるようにする)
        objective = pp.lpSum(self.number_list[i][j] * y[i, j] for i in range(self.n) for j in range(self.n) if i!= j )
                        
        problem += objective
        #print(problem)
 
        # 制約条件1(参加者は、１つのグループに割り当て)
        for i, s in enumerate(self.status):
            if s == True:
                problem += pp.lpSum([x[i, g] for g in self.group_list]) == 1

        # 制約条件2(各クラスは、min~max人)
        for g in self.group_list:
            problem += pp.lpSum([x[i, g] for i, s in enumerate(self.status) if s == True]) >= self.min_member
            problem += pp.lpSum([x[i, g] for i, s in enumerate(self.status) if s == True]) <= self.max_member
            
        # 制約条件3(変数xと変数yの関連付け、同じグループならyが１になる。)           
        for g in self.group_list:
            for i in  range(self.n):
                for j in range(self.n):
                    if i != j:
                        problem += x[i, g] + x[j, g] -1 <= y[i, j]
        
        #print(problem)
        
        # 最適化の実行
        status = problem.solve()
        
        # 結果の把握
        print("Status: {}".format(pp.LpStatus[status]))
        # 最適化計算の結果
        group_result = {}
        belong_result = {}
        
        for g in self.group_list:
            group_result[g] = [i for i, s in enumerate(self.status) if ((s == True) & (x[i,g].value()==1))]
        
        for i, s in enumerate(self.status):
            if s == True:
                belong_result[i] = [g for g in self.group_list if x[i,g].value() == 1][0]
        
        return group_result, belong_result