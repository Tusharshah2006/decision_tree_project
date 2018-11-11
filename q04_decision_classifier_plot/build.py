# %load q04_decision_classifier_plot/build.py
# default imports
from sklearn.model_selection import RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.switch_backend('agg')

data = pd.read_csv('./data/loan_prediction.csv')
np.random.seed(9)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=9)

depth_list = [8, 10, 15, 20, 50, 100, 120, 150, 175, 200]


# Write your solution here :
def decision_classifier_plot(X_train, X_test, y_train, y_test, depth_list):
    train_mac = []
    test_mac = []
    
    for depth in depth_list:
        dtc = DecisionTreeClassifier(max_depth=depth, random_state=9)
        dtc.fit(X_train, y_train)
        
        y_train_pred = dtc.predict(X_train)
        train_mac.append(accuracy_score(y_train, y_train_pred))
        
        y_test_pred = dtc.predict(X_test)
        test_mac.append(accuracy_score(y_test, y_test_pred))
    
    plt.plot(depth_list,train_mac)
    plt.plot(depth_list,test_mac)
    plt.show()

decision_classifier_plot(X_train, X_test, y_train, y_test, depth_list)


