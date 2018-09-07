from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
iris = load_iris()

iris = load_iris()
test_idx = [0,50,100]

#training data
train_target = np.delete(iris.target,test_idx)
train_data = np.delete(iris.data,test_idx,axis=0)

test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)
print(test_target)
print(clf.predict(test_data))
#viz code
from sklearn.externals.six import StringIO
import pydot
from graphviz import Graph
from IPython.display import Image

dot_data = StringIO()
tree.export_graphviz(clf,
                     out_file=dot_data,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True,rounded=True,
                     impurity=False)

graph= pydot.graph_from_dot_data(dot_data.getvalue())
#Image(graph.create_png())
g = Graph(format('png'))
g.
graph.write_pdf("iris.pdf")
graph[0].write_pdf("iris.pdf")
#graph[0].write_pdf("iris.pdf")
