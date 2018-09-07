#first lesson from sentdex

import quandl,math
from sklearn import preprocessing, cross_validation,svm
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

# X = features
# Y = label
df = quandl.get('WIKI/GOOGL')
#print(df.head) - brings back all columns
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open'] * 100.0

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]  #features
forecast_col = 'Adj. Close'
df.fillna(-99999,inplace=True) # used to replace N/A
forcast_out = int(math.ceil(0.1*len(df))) # forcasting days ago
df['label'] = df[forecast_col].shift(-forcast_out) # label is prediction
df.dropna(inplace=True)
print(df.head())
#X  is features
#y is labels
X = np.array(df.drop(['label'],1))
y = np.array(df['label'])
X = preprocessing.scale(X)
#X = X[:-forcast_out+1]
df.dropna(inplace=True)
y = np.array(df['label'])
X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y,test_size=0.2)
#ML alogs  SVr = support vector regression
clf = LinearRegression()
clf2 = svm.SVR()
clf3 = svm.SVR(kernel="poly")
clf.fit(X_train,y_train) # fit is train
clf.score(X_test,y_test) #score is test
clf2.fit(X_train,y_train)
clf2.score(X_train,y_train)
clf3.fit(X_train,y_train)
clf3.score(X_train,y_train)

accuracy = clf.score(X_test,y_test)
accuracy2 = clf2.score(X_test,y_test)
accuracy3=clf3.score(X_test,y_test)
print(accuracy)
print(accuracy2)
print(accuracy3)


