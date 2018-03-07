# 回溯问题

> 在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根结点出发深度探索解空间树。当探索到某一结点时，要先判断该结点是否包含问题的解，如果包含，就从该结点出发继续探索下去，如果该结点不包含问题的解，则逐层向其祖先结点回溯。（其实回溯法就是对隐式图的深度优先搜索算法）。 若用回溯法求问题的所有解时，要回溯到根，且根结点的所有可行的子树都要已被搜索遍才结束。 而若使用回溯法求任一个解时，只要搜索到问题的一个解就可以结束。--《百度百科》





## 回溯法设计思想

在回溯法执行时，应当：

- 保存当前步骤，如果是一个解就输出；
- 维护状态，使搜索路径（含子路径）尽量不重复。必要时，应该对不可能为解的部分进行剪枝(pruning)。



## 一般实现框架

- 核心变量：记录部分解answer[]、搜索深度k

- 核心函数：

  - is_a_solution(): 判断当前部分解是否是一个符合要求的解
  - construct_candidates(): 根据目前状态，构造下一步可能的选择
  - process_solution(): 对符合条件的解进行处理，通常是输出、计数等
  - make_move()和unmake_move(): 更新原始数据结构和取消更新

- 大致框架：

  ```python
  def backtrack(k):
    if is_a_solution():
      process_solution()
     else:
      k = k + 1
      candidates = construct_candidates()
      for candidates in candidates:
        makemove()
        backtrack(k)
        unmake_move()
        if finished:
          return
  ```

  ​

## 算法练习

- [问题1：求一个集合的所有子集](https://github.com/clhchtcjj/Algorithm/blob/master/backtrack/fullset.py)
- [问题2：输出不重复数字的全排列](https://github.com/clhchtcjj/Algorithm/blob/master/backtrack/fullset.py)
- [问题3：求解数独](https://github.com/clhchtcjj/Algorithm/blob/master/backtrack/shudu.py)
- [问题4：给定字符串，生成其字母的全排列](https://github.com/clhchtcjj/Algorithm/blob/master/backtrack/fullstring.py)
- [问题5：求一个n元集合的k元子集](https://github.com/clhchtcjj/Algorithm/blob/master/backtrack/k-subset.py)
- [问题6：8皇后问题](https://github.com/clhchtcjj/Algorithm/blob/master/backtrack/eightqueen.py)

持续更新....
