# Visualizing a decision tree
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
print(iris.feature_names)
print(iris.target_names)
# print (iris.data[0])
# print (iris.target[0])
test_idx = [0, 50, 100]  # 3 types pf flower starting at 0,50 and 100
# training data
# for i in range (len(iris.target)):
#    print("Example %d: label %s, features %s" %(i,iris.target[i],iris.data[i]))
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)
# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)
print(test_target)  # print 0,1,2 - these are what the predicted flower could be
print(clf.predict(test_data))

# viz code
from sklearn.externals.six import StringIO
import pydotplus
#import graphviz
from IPython.display import Image
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
#from sklearn import tree

dot_data = StringIO()

tree.export_graphviz(clf, out_file=dot_data,
                     feature_names=iris.feature_names, class_names=iris.target_names,
                     filled=True, rounded=True, impurity=False)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
#graph.write_pdf("test.pdf")
graph.write_pdf("boots.pdf")
#Image(graph.create_png("test.png"))
#pydotplus.graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
#Image(pydotplus.Graph.create_png("test.png"))
#pydotplus.graph.write_pdf("Iris.pdf")
#pydotplus.graph_from_dot_data()

