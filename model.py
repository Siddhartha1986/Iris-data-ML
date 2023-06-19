import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import joblib

#random seed
seed = 42

#Read oroginal dataset
iris_df = pd.read_csv("data/iris.csv")
#iris_df.sample(frac = 1, random_stat = seed)

#Selecting features and target data
X = iris_df[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]]
y = iris_df["Species"]

#Split data into train and test sets
# 70% training and 30 % test

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3,random_state=seed, stratify = y)

#Create and instance of the k neighbours classifier
clf = KNeighborsClassifier(n_neighbors=10)

#train the classifier on the training data
clf.fit(X_train, y_train)

#predict on the test set
y_predict = clf.predict(X_test)

#claculate the accuracy

accuracy = accuracy_score(y_test,y_predict)
print(f"Accuracy: {accuracy}")   # Accuracy: 0.91

joblib.dump(clf,"output_models/rf_model.sav")