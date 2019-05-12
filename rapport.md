# MAIN RESULTS

## 1. The best algorithm: 
 
 'weka.classifiers.trees.RandomForest' with parameter ['-K', 4] ( average accuracy result is approximately 0.885219 )

 Moreover, this algorithm with others parameters also give the accuracy score which is very well.
 ***So I suggest us apply this algorithm on our model.*** 

## 2. The worst algoritm:

 'weka.classifiers.functions.MultilayerPerceptron' with parameter ['-H', '24,24,12', '-N', '150', '-L', '0.1', '-V', '20', '-E', '10'] 
 
 And with others parameters, this algorithm don't give the good result. ***So don't chose this algorithm.***

## 3. The dataset:

|       Description      |    Dataset    | Average accuracy |
|:----------------------:|:-------------:|:-------------:|
| The easiest dataset    |    'badges2'    |    0.998830   |
|   The hardest dataset  | 'primary-tumor' |    0.366166   |

## 4. The NaN value:

 * The algo "weka.classifiers.bayes.BayesNet" with parameter '['-Q', 'weka.classifiers.bayes.net.search.local.LAGDHillClimber', '-E', 'weka.classifiers.bayes.net.estimate.BMAEstimator']' has a bad result ( 70 Nan Values ) but with others parameters, it has a few NaN values. ***So, the selection of parameters for each algorithm is very important.***
 * The dataset "mfeat-pixel" has the most values ( 17 NaN values ). I try to open this dataset, I see that there're many value 0. It's not natural. ***So, the approach to analyze our model is heavily depenent on the nature of the dataset.***
 * Most datasets have at least 1 value null ( 50% ), and there are also no many NaN values ( total is 72 NaN values in our model). ***So this missing values don't cause errors in our general model.***  

## 5. Optimal parameters for each algorithm:

|       Algorithm       |                                                       Best Parameter                                                       | Average Accuracy |
|:---------------------:|:--------------------------------------------------------------------------------------------------------------------------:|------------------|
|        BayesNet       | ['-Q', 'weka.classifiers.bayes.net.search.local.HillClimber', '-E', 'weka.classifiers.bayes.net.estimate.SimpleEstimator'] | 0.865083         |
|      Naive Bayers     | ['-K']                                                                                                                     | 0.840289         |
|       Rule Parts      | ['-C', 0.15, '-M', 2]                                                                                                      | 0.862190         |
|       Rules Jrip      | ['-N', 2]                                                                                                                  | 0.861247         |
|       Trees J48       | ['-M', 2]                                                                                                                  | 0.816474         |
|      Random Tree      | []                                                                                                                         | 0.802317         |
|     Random Forest     | ['-K', 4]                                                                                                                  | 0.884717         |
| Multilayer Perceptron | ['-H', '100', '-N', '100', '-L', '0.1', '-V', '20', '-E', '10']                                                            | 0.821361         |
|          IBk          | ['-K', 5]                                                                                                                  | 0.817839         |
|          OneR         | ['-B', 8]                                                                                                                  | 0.633414         |
|    Simple Logistic    | []                                                                                                                         | 0.865376         |
|        Logistic       | ['-M', 300]                                                                                                                | 0.839286         |
|          SMO          | []                                                                                                                         | 0.850218         |