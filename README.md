# Myers Briggs Machine Learning Project

[![All Contributors](https://img.shields.io/badge/contributors-4-green.svg?style=flat-square)](#contributors-) ![Developement](https://img.shields.io/badge/progress-in%20development-orange)

## Topic and Background
*The topic*
??? Steven ???

*Reasons why we selected our topic:*

Myers-Briggs Type Indicator (MBTI) is one of the most prevalent personality tests in the world. Its purpose is to categorize psychological profiles based on the assumption that variations in everyday behavior are ordered, consistent, and capable of being categorized. Currently, the MBTI test is performed by an online quiz. 

However, these tests often include intrinsic biases because the subject is conscious of the quiz processes and will answer accordingly. Therefore, we wanted to create a more objective process for testing MBTI. By inputting writing from the subject, we hope to train a machine learning model to predict his personality category through text analytics. Hopefully, this will eliminate input biases from the subject.

## Data Source
The Myers Briggs Type Indicator (or MBTI for short) is a personality type system that divides everyone into 16 distinct personality types across 4 axis: 
- Introversion (I) – Extroversion (E) 
- Intuition (N) – Sensing (S) 
- Thinking (T) – Feeling (F) 
- Judging (J) – Perceiving (P) 

The dataset contains ~8600 observations (people), where each observation gives a person’s: 
- Myers-Briggs personality type (as a 4-letter code) 
- An excerpt containing the last 50 posts on their PersonalityCafe forum (each entry separated by “|||”) 

This data was collected through the PersonalityCafe forum, as it provides a large selection of people and their MBTI personality type, as well as what they have written. 

## Questions to answer with the data
- Explore and analyze the data to see if any patterns can be detected in specific types and their style of writing, which overall explores the validity of the test in analysing, predicting or categorising behaviour. These include:
    - Length of the post (word count)
    - Length of average sentences (word count)
    - Use of stop words, punctuation (count)
- Create a Machine Learning model that is able to predict the personality type based on the writing input

## Machine Leaning Model
*1. Which model and why*
- We choose Random Forest model.
- Random Forest model is a good fit for our data structure (tabular). It can produce a result much faster compared to Neural Network model. 
- Among other model options, SVM is our second choice, but it requires the feature to be straight forward while ours is not. Logistics regression works well with a smaller dataset but our dataset will have thousands of features and observations. 
- For learning purpose, we will also try out these model options and compare their accuracy.

*2. How to train the model*
- We will use `train_test_split` to split the data into `X_train`, `X_test`, and `y_all_train`, `y_all_test`. 
- `X_train` and `X_test` includes all the features
- `y_all_train` and `y_all_test` include four columns of target label
- When training, we will run the model four times. In each iteration, we will use the same `X_train` with one column (target) from the `y_all_train`. Running the model four times will generate four labels for each test observation. 

*3. What are the target label(s)*
- Each observation will have four initial labels, one from each of the below binary combination:
    - "E-I"
    - "N-S"
    - "T-F"
    - "J-P"
- Depending on the final presentation of the dashboard, we may either keep the four labels separate, or group together into 16 possible variations.

## Communication Protocol
Our main media of communication are currently: 
1.    Slack (Standard Communication)
2.    Zoom (Meetings)
3.    Individual phone numbers (Emergencies)
- As our primary medium of communication, we will use Slack, where we will communicate our day-to-day logistics.
- Our bi-weekly meetings, usually after 6PM ET, are organized through individual Zoom calls. This is where we will get connected, see everyone’s progress, and plan work for the upcoming few days.
- In case of emergency, we will call or text one another, depending on the urgency of the situation.

## Technologies Used
* Python (Pandas)
* Sklearn
* Bootstrap
* Flask
* JavaScript
* HTML/CSS



