from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score

def simple_churn_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    clf = LogisticRegression(max_iter=500)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    prob = clf.predict_proba(X_test)[:,1]
    return {'accuracy': accuracy_score(y_test, preds), 'auc': roc_auc_score(y_test, prob)}
