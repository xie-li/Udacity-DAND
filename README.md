### data types：
#### quantitative data ： numeric values that allow mathematical operations
###### divide quantitative data types further into two type:
1. continous data : quantitative values that can be split into smaller values
2. discrete data : that are countable
#### category data：a group or a set of items
###### divide categorical data types further into two types:
1. categorical ordinal(ordered):categorical data that are ranked
2. categorical nominal(no order):that do not have ranked order

![image](http://note.youdao.com/yws/res/1004/E4E938FF4D1D43C288417F6C3BC71BA4)

### simple linear regression
> a linear comparison of only two quantitative variables 

### statistc
#### measure of center
1. mean
2. median
3. mode
#### measure of spread
1. range
2. interquartile range (IQR)
3. Standard Deviation
4. Variance

#### measure of shape
#### measure of outliers

###### 数据分析过程组织为五个步骤：提问、整理、探索、得出结论和传达结果
1. question
2. wrangle:gather、assess、clean
3. explore
4. draw conclusions
5. communicate

##### 当出现异常值时，我们应该考虑以下几点。
1. 注意到它们的存在以及对概括性度量的影响。
2. 如果有拼写错误 —— 删除或改正。
3. 了解它们为什么会存在，以及对我们要回答的关于异常值的问题的影响。
4. 当有异常值时，报告五数概括法的值通常能比均值和标准差等度量更好地体现异常值的存在。
5. 报告时要小心。知道如何提出正确的问题。

#### binary distribution
#### conditional probability

#### total probability
#### bayes rule
> given an initial prediction,if we gather additional related data,data that our prediction depends on,we can improve that prediction


#### descriptive statistics
> 是用来描述收集的数据

#### inferential statistics
> drawing conclusions about a population base on data collected from a sample of individuals from that population



1. 总体 - 我们想要研究的整个群体
2. 参数 - 总体的数值摘要
3. 样本 - 总体的一个子集
4. 统计量 - 样本的数值摘要

![image](http://note.youdao.com/yws/res/1054/3E0933A27CA043DAA1B0B0002E404B89)

#### law of large numbers
#### central limit theorem

#### 抽样分布
- 抽样分布 是一个统计量 (任何统计量) 的分布。
- 抽样分布涉及两个重要数学定理：大数法则 和 中心极限定理。
- 大数法则 表示随着样本容量增加，样本平均数越来越接近总体平均数。一般来说，如果统计量 "较好地" 估计参数，它会接近较大样本容量的参数。
- 中心极限定理 表示样本容量足够大，样本平均数会是正态分布，但是在多个样本平均数情况下，它才为真。

#### 自展法
- 自展法 是我们从群组中进行放回抽样的技巧
- 我们可以使用自展法，模拟在这节课进行多次的创建抽样分布。 
###### 通过自展法，计算我们统计量的重复数值，我们可以理解统计中的抽样分布。

###### 置信区间是针对总体中的 参数，而不是针对个别观测。
###### hypothesis tests and confidence intervals tell us about parameters not statistics

![image](http://note.youdao.com/yws/res/1123/ABAEC80ED845405FBA83998093F14683)

##### 常见的假设检验包括：

1. 测试总体平均数 (单样本 t 检验)。
2. 测试均数差 (双样本 t 检验)
3. 测试个体治疗前后的差异 (配对 t 检验)
4. 测试总体比例 (单样本 z 检验)
5. 测试总体比例的差异 (双样本 z 检验)

#### 什么是P值
> p 值是零假设为真时，得到统计量或更极端数值的概率。所以，p 值小，表示零假设不正确。相反，我们的统计量可能来自不同于零假设的分布。p 值很大时，我们可以证明统计量很可能来自零假设。所以我们无法证明拒绝零假设。通过对比 p 值和 I 类错误阈值 (α)，我们可以决定选择哪个假设。


```math
\\ p \leq \alpha => 拒绝H_0
\\ p > \alpha => 不拒绝H_0
```


##### scatter plot：
1. strength：weak moderate strong
2. direction：positive negative


##### correlation coefficient：measure the strength and direction of a linear relationship

![image](http://note.youdao.com/yws/res/1091/F858196E13DC41D49ACF37DF3EC84457)

###### intercept : 截距 the expected value of  the response when the explanatory variable is zero
###### slope ： 斜率 the expected change in the response for each 1 unit increase in the explanatory variable

###### 回归线通常由 截距 和 斜率 决定。
**截距**的定义为 当 x 变量为 0时，反应变量的预测值。  
**斜率**的定义为 x变量每增加一个单位引起的反应变量的预测变化。


```math
\\ \hat{y} = b_0 + b_1x_1
```


其中
y^为回归线反应变量的预测值。  
b<sub>0</sub>为截距。  
b<sub>1</sub>为斜率。  
x<sub>1</sub>为解释变量。  
y 为数据集某个数据点的实际反应变量值 (不是回归线的预测值)。  

##### fit a regression line:
> least squares algorithm : minimize the sum of the squared vertical distances from the line to points

##### 在多元线性回归里，我们要如何找到 “正确” 的系数
在简单线性回归那一节中，你知道了我们为什么要最小化每个实际数据点与模型预测值之间的平方距离。  
但在多元线性回归中，我们要找的数据点所处的空间实际上不仅仅是二维的。  
总而言之，重点在于我们可以计算 

```math
(X'X)^-X'y
 ```
，从而找出最优β 预测值。

##### interpreting multiple linear regression results

所有系数都为正值，因此我们可以将各系数解释为： 在模型其它变量不变的情况下，**解释变量每增加一个单位，反应变量会随之增加的预测幅度。**  
“在其它变量不变的情况下”，也就是说，只有当与系数有关的变量增加 1，反应变量才会变化，但其它变量都不会变化。  
***significant bivariate relationships are not always significant in multiple linear regression.***

#### dummy variable
要往线性模型里添加分类变量，就需要把分类变量转变为 虚拟变量。  
转化后，你需要舍弃一个 虚拟列，才能得到 满秩 矩阵。  
为了逆转 (X'X)，矩阵 X一定要是满秩的，也就是说，所有 X的列都必须线性独立。  
如果你要用 0 、1编码来创建虚拟变量，你就得舍弃一个虚拟列，确保所得矩阵是满秩的（这样你从 python 里得到的解才会是可靠的。）  
之所以要这么做，原因就在于线性代数的本质，更具体地说，要逆转矩阵，你手里的矩阵必须是满秩的 （也就是所有列都得线性独立），因此，你得舍弃掉一个虚拟列，方能得到线性独立的各列 （和一个满秩矩阵）。  


Problems in Mulitple Linear Regression:  
1. A linear relationship doesn`t exist
2. Correlated errors
3. Non-constant variance
4. Outliers
5. Multicollinearity

![image](http://note.youdao.com/yws/res/1185/BDAFD3C194414968A5A93755CF1C1FDD)

![image](http://note.youdao.com/yws/res/1184/448F1B330D6D4D6FA7F09489D95C5614)

#### logistic regression
**quantitative interpretations**:for every one unit increase in x1, we expect a multiplicative change in the odds of a 1 of e^b1  
**categorical interpretations**:when in catogory x1 , we expect a multiplicative change in the odds of a 1 by e^b1 compared to baseline  

