####谢明辉
1.20-1.23
掌握稀疏矩阵的用法，并编写了初步的潜在因子模型（随机梯度下降代码），但是仍有bug，训练溢出。

1.27 
通过调试发现每次的变化幅度太大导致失控，直接溢出。
后面大大降低了学习率发现学习效果良好，并且对比了训练前在测试集的预测误差总分和训练后的，发现有明显降低。

1.28
近期工作计划：将算法改写成类形式。

2.24
完善了对象的存储，将训练好的模型参数存储起来。

####李林
2.4-2.5
完成了首页数据请求的接口，调整了路由path并对django后台静态资源以及封面等资源路径进行了优化。

2.7-2.12
加入了Celebrity、History、MovieCategory等数据模型，并在Movie模型中增加了几个字段，同时优化了User模型。

2.25-2.27
完成了电影详情获取接口，对现有的数据模型全部进行了修改，去掉了部分冗余字段。  
新增电影类别表、电影标签表、电影角色表，并完成了相应的中间表连接工作，打通了与Movie相关的所有数据模型。
可以通过后台管理页面对数据模型进行管理了。

####梁跃