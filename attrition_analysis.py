from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report
import pandas as pd

df=pd.read_excel("WA_Fn-UseC_-HR-Employee-Attrition - Copy (2).xlsx")

df["Attrition"]=df["Attrition"].map({"Yes": 1, "No": 0})

print("Dataset shape:",df.shape)

print("\nAttrition counts after conversion:")
print(df["Attrition"].value_counts())

X=df.drop("Attrition",axis=1)
y=df["Attrition"]

print("\nFeatures shapes:",X.shape)
print("target shape:",y.shape)

print("\n datatypes:")
print(X.dtypes)

print("\n print categorial columns and their unique values:")

for column in df.select_dtypes(include="str").columns:
    print("\n",column)
    print(df[column].unique())

print("\nNumerical columns summary:")
print(df.describe())

print("\ncorrelation with attrition:")
print(df.corr(numeric_only=True) ["Attrition"].sort_values(ascending=False))

categorical_columns=df.select_dtypes(include="str").columns

print("\ncategorical columns:")
print(categorical_columns)

for column in categorical_columns:

    print("\n==========================")
    print("\n",column)

    print("=========================")
    print(pd.crosstab(df[column],df["Attrition"],normalize="index")*100)

from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)


print("training data:",X_train.shape)
print("testing data:",X_test.shape)

categorical_columns=X.select_dtypes(include="str").columns

preprocessor=ColumnTransformer(transformers=[
    ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_columns),
],
remainder="passthrough"
)

print("categorical columns:")
print(categorical_columns)

model=Pipeline(steps=[
    ("preprocessor", preprocessor),("classifier", LogisticRegression(solver="liblinear",max_iter=5000,class_weight="balanced"))
])

model.fit(X_train,y_train)

print("model training completed")

y_pred=model.predict(X_test)
print("\npredictions completed")

from sklearn.metrics import accuracy_score

accuracy=accuracy_score(y_test,y_pred)

print("model accuracy:",accuracy)
print("accuracy percentage:",accuracy*100)

cm=confusion_matrix(y_test,y_pred)

print("\nconfusion matrix:")
print(cm)

print("\nclassification matrix:")
print(classification_report(y_test,y_pred))

import joblib
joblib.dump(model,"employee_attrition_model.pkl")
joblib.dump(preprocessor,"employee_attrition_preprocessor.pkl")

print("\nmodel saved successfully")
