# LeetCode No.210
from collections import deque, defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        # 入力辺、出力辺のそれぞれに対してグラフを用意する
        in_degrees, out_degrees = defaultdict(list), defaultdict(list)
        arr, s = [], set(list(range(numCourses)))

        for edge in prerequisites:
            dst, src = edge[0], edge[1]
            out_degrees[src].append(dst)
            in_degrees[dst].append(src)

            # 入力辺を持つノードを除外
            if dst in s:
                s.remove(dst)

        # 入力辺を持たないノードをqに入れる
        q = deque(list(s))

        # 入力辺を持たないノードがなくなるまで繰り返す
        while q:
            node = q.popleft()
            arr.append(node)

            # 隣接ノードを走査
            for adj in list(out_degrees[node]):
                # nodeからの入力辺を削除
                in_degrees[adj].remove(node)

                # 隣接ノードの入力辺の数が0になった場合、qに追加する
                if len(in_degrees[adj]) == 0:
                    q.append(adj)

            # nodeをグラフから削除
            del out_degrees[node]

        # グラフから全てのノードが削除されていればトポロジカルソート完了
        if len(out_degrees) == 0:
            return arr
        # グラフに入力辺を持つノードが残っている場合、閉路が存在する（トポロジカルソート不可）
        else:
            return []



