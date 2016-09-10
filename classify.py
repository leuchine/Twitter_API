import sys
import os
import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier 


if __name__ == '__main__':
    classes = ['pos', 'neg']
    dataset=[]
    label=[]
    # Read the data
    with open('travel.csv') as f:
        for i in f:
            dataset+=[i.split(';;')[0]]
            label+=[classes[0]]
    with open('sample.csv') as f:
        for i in f:
            dataset+=[i.split('\t')[2]]
            label+=[classes[1]]
            if len(label)>6000:
                break;

    train_data, test_data, train_labels, test_labels=\
    train_test_split(dataset, label, test_size=0.25, random_state=32)
    
   
    # Create feature vectors
    vectorizer = TfidfVectorizer(min_df=5,
                                 max_df = 0.8,
                                 sublinear_tf=True,
                                 use_idf=True)
    train_vectors = vectorizer.fit_transform(train_data)
    test_vectors = vectorizer.transform(test_data)

    # Perform classification with SVM, kernel=rbf
    classifier_rbf = RandomForestClassifier(n_estimators = 20)
    #classifier_rbf = svm.SVC()
    
    classifier_rbf.fit(train_vectors.toarray(), train_labels)
    
    prediction_rbf = classifier_rbf.predict(test_vectors.toarray())
    print(classification_report(test_labels, prediction_rbf))
    print(test_labels[:5])
    print(prediction_rbf[:5])
