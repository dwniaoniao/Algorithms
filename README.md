## K路归并 KMerge
把 k 个有序表合并成一个有序表，元素共有 n 个。  
每个表的元素都是从左到右移入新表；  
把每个表的当前元素放入二叉堆中，每次删除最小值并放入新表中，然后加入此序列的下一个元素；

## 精明的玩家 Smart Player
**关键词**： 动态规划问题、背包问题

### 问题描述
有n(n<=51) 种装备，每种装备会增加英雄一定的力量。装备分基本和高级两种，基本装备可以直接用金币购买，
而一种高级装备需要用固定种类和数量的较低级装备来合成，装备的合成路线可以用一棵树来表示。每
件基本装备都有数量限制（不超过100），这限制了你不能无限制地合成某些性价比很高的装备。
现在，英雄Spectre 有m(m<=2000) 个金币，他想用这些金钱使自己的力量值尽量高。

### 输入
对于如下的输入，第一行从左向右分别表示所有装备类型、基本装备、高级装备的数目和 玩家拥有的金币数目，记基本装备数量为 b，高级装备的数量为 p，接下来的 b 行从左向右分 别表示标志基本装备名称的数字、该装备的力量值、所值的金币和最大数量限制。再接下来的 p 行从左向右分别表示标志高级装备名称的数字、合成该装备所需的所有装备的编号以及合成 后该装备所具有的额外力量值。  
```
4 2 2 5 
1 1 1 2
2 2 2 2
3 1 2 5
4 2 3 10
```

### 输出
对于上面的输入例子，其输出如下，第一行的数字即为所求的最大力量值，中括号中的数字表示得到该最大力量值所使用的所有装备。
```
20
[4]
```

## 排序 Sort
- 输入：可排序的序列a[0...n-1]
- 输出：升序排序的序列a[0...n-1]
