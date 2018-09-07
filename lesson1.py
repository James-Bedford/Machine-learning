" lesson 1 "
"apple or an orange supervised learning using decision tree recipe 1"

from sklearn import tree


features = [[140],[130],[150],[170],[200]]
"labels = [0,0,1,1]"
labels = ["apple","apple","orange","orange","water melon"]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print (clf.predict([[185.1]]))