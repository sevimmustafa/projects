# %%
"""

Homework 1
1) How would you define Machine Learning?
2) What are the differences between Supervised and Unsupervised Learning?
Specify example 3 algorithms for each of these.
3) What are the test and validation set, and why would you want to use them?
4) What are the main preprocessing steps? Explain them in detail.
Why we need to prepare our data?
5) How you can explore countionus and discrete variables?
6) Analyse the plot given below. (What is the plot and variable type,
check the distribution and make comment about how you can preproccess it.)
"""
# %%
"""
Answers 1
1. It is a sub-component of the Artificial Intelligence. Basically, It offer us an algorithm that
predict output via training the dataset given beforehand.
2. In supervised learning, we give the machine both input (features) and outputs (labels) as a dataset
and then we expect from machine to offer us an algorithm via train-test-split method. "Regression" and "Classification"
are two types of supervised machine learning techniques. However, in unsupervised learning, we give the machine only
inputs and then we expect from the machine offer us an algorithm. "Clustering" and "Association" are two types of
unsupervised learning.
    2.a. Examples of supervised learning: Predict the expected lifespan via blood pressure, blood cholesterol, blood
    glucose, waist circumferences, serum ALT, serum AST values of a person.
    2.b. Examples of unsupervised learning: To forecast a possible similarity with a given disease via some molecular
    markers.
3. Due to establish an algorithm, the machine is required to a training set. For this reason 30% of the whole dataset
is used by machine. Then, machine testing the power of algorithm which already establish via rest of the data set.
Once an algorithm has been created, given a new data, machine divide the data into training, validation and
testing sets. Then, it checks the algorithm's validity by validation. Also there is one more method that named
"Cross Validatin". This method conduct the train-validity-test process at once.
4. Machine Learning is often using complicated and large datasets. By nature, this kind of datasets includes
very vary data. However, to obtain a useful algorithm and avoid errors, we must use homogenous and appropriate data.
Therefore, before using the dataset, we should explore the dataset and fix the problems.(Exploratory Data Analysis(EDA))
For this purpose, there are seven main steps:
    4.a. Duplicate values: Dataset should investigate and than, it should be clear the duplicate values to avoid
    4.b. Imbalanced data: Some dataset involve more than one classes. And sometimes variable of one class of this
    dataset should be extremely more or less than other. In this case, we should use "oversampling" or "undersampling"
    method to fix this distortion.
    4.c. Missy value: Sometimes a dataset may include many null index. To fix this problem we can use either "Eleminate
    missing values" or "Filling with mean or median" method. For this last method, if our values is normally distribute
    we fill the null index with mean of the values. if our values is not normally distribute we fill the null index
    with median of the values.
    4.d. Determine the outlier: For clear the marginal values this method should be used.
    4.e. Feature scaling: It can be use for normalisation or standardization the our values.
    4.f. Feature extraction: It is to obtain useful, calculable information from the information in the dataset.
    4.g. Feature encoding: It is a method that used for transforming the nominal or ordinal data to able to use in
    the machine learning process.
5. It can be explored two ways:
    5a. By determining the property of data. If a variable can take any numeric value, it is called a continuous
    variable. On the other hand, if a variable can take only integer or categorical value and can not divide, it is
    called a discrete value.
    5b. By drawing the histogram. If we draw the histogram and observed the continuous variable distribution, we assume
    that our variable type is continuous.
6. This plot is a histogram, and the variable type of this plot is continuous. The distribution of this plot is not
symmetrical. So outlier detection and a normalisation technique is necessary.
