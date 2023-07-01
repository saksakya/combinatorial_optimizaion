import math
import pulp as pp

class find_combination(object):
    def __init__(self, nl, status, max_menber, min_menber):
        self.number_list = nl
        self.status = status
        # self.n = len(nl)
        self.max_menmber = max_menber
        self.min_menber = min_menber
        self.group_nums = math.ceil((status == True).sum() / max_menber)

    def calc(self):
        problem = pp.LpProblem('combination',pp.LpMinimize)
        # n = self.n

        # 変数の定義 (Memo binary:0or1 continuous:low:1~up:nまでの連続値)
        # x = [[pp.LpVariable("x(%s,%s)"%(i, j), cat="Binary") for i in range(N)] for j in range(N)]
        # u = [pp.LpVariable("u(%s)"%(i), cat="Continuous", lowBound=1.0, upBound=(N)) for i in range(N)]

        #print(x)
        #print(u)

        # 目的条件(グループで一緒になった回数の総和)
        # objective = pp.lpSum(self.dm[i][j] * x[i][j] for i in range(N) for j in range(N) if i != j)
        # problem += objective

        # # 制約条件1(制約条件1と2で各地点1回ずつしか通らない条件)
        # for i in range(N):
        #     problem += pp.lpSum(x[i][j] for j in range(N) if i != j) == 1

        # # 制約条件2
        # for i in range(N):
        #     problem += pp.lpSum(x[j][i] for j in range(N) if i != j) == 1

        # # 制約条件3(MTZ制約)
        # for i in range(N):
        #     for j in range(1,N):
        #         if i != j:
        #             problem += u[i] + 1.0 - self.BigM * (1.0 - x[i][j]) <= u[j]
                    
        # # print(problem)
        
        # # 最適化の実行
        # status = problem.solve()
