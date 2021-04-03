from sklearn import datasets
from sklearn import svm

iris = datasets.load_iris()
print(iris.data.shape)

model = svm.LinearSVC()

model.fit(iris.data, iris.target)                 # 训练模型
model.predict()             # 预测新样本
model.score()               # 得分

print(model)
