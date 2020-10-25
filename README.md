# Myers-Briggs Machine Learning Project

[![All Contributors](https://img.shields.io/badge/contributors-4-green.svg?style=flat-square)](#contributors-) ![Developement](https://img.shields.io/badge/progress-in%20development-orange)


## Presentation
* The PowerPoint contains a more detailed discussion of the trials and errors of the machine learning models.
* This file can be accessed [here](https://docs.google.com/presentation/d/1YATOfX2lsJnDj15BejmGqwXvXYVGnL30jpCSBRJUk5c/edit?usp=sharing).

## Topic and Background
Personality

**Reasons why we selected our topic:**

Myers-Briggs Type Indicator (MBTI) is one of the most prevalent personality tests in psychology. Its purpose is to classify psychological profiles based on the assumption that variations in everyday behavior are ordered, consistent and capable of being categorized. Currently, the MBTI test is performed by an online quiz. 

However, these tests often include intrinsic biases because the subject is conscious of the quiz's processes and will answer accordingly. Therefore, we wanted to create a more objective process for testing MBTI. By inputting writing from the subject, we hope to train a machine learning model to predict their personality category through text analytics. Hopefully, this will eliminate input biases from the subject.

## Data Source
The Myers-Briggs Type Indicator (MBTI) is a taxonomy that divides everyone into 16 distinct personality types across four axes: 
- Introversion (I) – Extraversion (E) 
- Intuition (N) – Sensing (S) 
- Thinking (T) – Feeling (F) 
- Judging (J) – Perceiving (P) 

The dataset contains ~ 8,600 observations (people), where each observation gives a person’s: 
- Myers-Briggs personality type (as a 4-letter code)
- An excerpt containing the last 50 posts on their PersonalityCafe forum (each entry separated by “|||”)

This data was collected from the PersonalityCafe forum, as it provides a large selection of people and their MBTI personality types, as well as what they have written. 

## Questions to answer with the data
- Explore and analyze the data to see if any patterns can be detected in specific personality types and their writing styles. This explores the validity of the test in analyzing, predicting and categorizing behavior. These include:
    - Length of the post (word count)
    - Length of average sentences (word count)
    - Use of stop words and punctuation (count)
- Create a Machine Learning capable of predicting the user's personality type based on their writing input.

## Tools and Technologies Used
* PostgreSQL
* AWS RDS
* Python
* Sklearn
* Bootstrap
* Flask
* HTML/CSS

## Database setup:
**AWS ADS**
- Set up RDS instance on AWS, and connect it to PostgreSQL

**Postgres** 
- Create new server with RDS as the host
- Create SQL table and import data in .csv format

**SQLAlchemy**
- Set up connection with Postgres database
- Reads in the table as a Pandas Dataframe

## Exploratory Data Analysis 
**1. What does the data look like?**
- A personality type count shows that the sample data is not very evenly distributed.
- Four data types, INFJ, INFP, INTJ and INTP have considerably larger samples (more than 1,000) than ESFJ, ESFP, ESTJ and ESTP (fewer than 250).
- The users from the forum tend to be IN?? type.

![typeCount](/Resources/mdImages/analysis/type_count.png)

**2. Are each dimensions balanced?**
- Comparing the sample sizes within each of the four axes, we can see that the E-I and N-S axes have extremely imbalanced sample sizes.

![classImbalance](/Resources/mdImages/analysis/class_imbalance.PNG)


**3. Does each group have some difference?**
- We counted the use of urls, exclamation marks, question marks, word length and digits per post for each personality type.
- The use of exclamation marks and http links differ slightly among the  groups. Other writing style counts tend to be fairly evenly distributed.

![features](/Resources/mdImages/analysis/features.PNG)


**4. Are the four dimensions independent?**
- There are 16 personality types, and this limits our choice of Machine Learning models. 
- We proposed dividing the personality types into four axes (E-I, N-S, F-T and J-P).This way, our model only needs to output a binary result. This widened our selection of models considerably.
- Before going forward, we need to test the assumption that each of the four axes is independent from the others.
- A correlation matrix is produced, as shown in the figure on the left.
- Overall, the correlations’ absolute values are < 0.2, indicating low correlation.

![typeCorr](/Resources/mdImages/analysis/type_corr.png)


## Data Cleaning
**1. What to clean up**
- Used RegEx methodology to clean data that consisted of social media posts from over 8,000 unique identifiers with 50 posts each separated by 3 pipes ( ||| ). 
- Reading the mood from text with ML is called “sentiment analysis.” However, before we could perform sentiment analysis, we had to create a column without the following: http strings; ||| strings; punctuation marks; underscores; numbers; one letter words; leftover white space. 
- Then, we made everything lowercase. 

**2. The balance of information and noise**
- We decided that because we are trying to predict personality types, we wanted the text as similar to the actual writing as possible; this is part art and part science.
- We then tokenized and performed TF-IDF vectorization for the cleaned text, and used all 17,000 features as model input. 


## Machine Learning Model
**1. Which models**
- We tried five different models: Logistics Regression; Neural Network; Random Forest; Linear SVC; LinearSVC with KBInsDiscretizer.
- With further improvements, the Logistics Regression model produced the best result in terms of overall F1 score and accuracy.

**2. How to train the model**
- We will use `train_test_split` to split the data into `X_train`, `X_test`, and `y_all_train`, `y_all_test`. 
- `X_train` and `X_test` include all 17,000 features that are vectorized from the cleaned text input.
- `y_all_train` and `y_all_test` include four columns of target labels.
- When training, we will run the model four times. In each iteration, we: 
    - Resample the data for each dimention to solve the class imbalance issue.
    - Use the resampled `X_train` with one column (target) from the `y_all_train`.
    - Run the model four times to generate four labels for each test observation.

**3. What are the target label(s)**
- Each observation will have four initial labels, one from each of the following binaries:
    - "E-I"
    - "N-S"
    - "T-F"
    - "J-P"

## The Application
**1. Objective of the app**

We want to let users try the model themselves by entering an example of their writing in the text box to receive a prediction of their personality type. 

**2. The Front-end content**
- A text box where the user can input their writing. For better accuracy, there is a minimum requirement of 150 characters.
- A `predict` button to click on when the user is ready to view the result.
- A background introduction of Myers-Briggs Type Indicators with the meaning of each dimension.
- A brief bio of the creators and the background of this project.

**3. The Back-end**
- Workflow

![appFlowChart](/Resources/mdImages/app_workflow.PNG)

- Model weights and other variables
    - After running the logistics regression model, we used `pickle` to save the weights of our four models.
    - Since we need to preprocess the user text input, we also needed to save the `vectorizer` variable.
- Flask
    - Import all four model weights and the `vectorizer` variable.
    - Initiate a Flask app.
    - Create a root route using our HTML template.
    - Use a `POST` method to capture the user input in the text box.
    - Apply regex cleaning and vectorize the text into features.
    - Input the features into four models and get predicted results for four dimensions.
    - Convert 1 & 0 binary results to corresponding personality type letters.
    - Output the four dimensions back to the frontend in the result section.
- HTML
    - At the text box section, we included `<form action="{{ url_for('predict')}}" method="POST">` so it can be called from Flask.
    - In the result section, we included `{{ prediction_text }}` so the prediction result can be reflected.

**4. A Preview**
![FontEnd1](/Resources/mdImages/frontEnd/FrontEnd_1.png)
![FontEnd2](/Resources/mdImages/frontEnd/FrontEnd_2.png)
![FontEnd3](/Resources/mdImages/frontEnd/FrontEnd_3.png)
![FontEnd4](/Resources/mdImages/frontEnd/FrontEnd_4.png)
![FontEnd5](/Resources/mdImages/frontEnd/FrontEnd_5.png)
![FontEnd6](/Resources/mdImages/frontEnd/FrontEnd_6.png)
![FontEnd7](/Resources/mdImages/frontEnd/FrontEnd_7.png)

## Segment 3 Roles:
During Segment 3, we seperated into different roles than those suggested by the rubric. We wanted to do this because our delegation of tasks was more conducive to a smooth workflow:

**Davenel Denis:**
- Developed Neural Net model
- Updated Random Forest model with Resampling
- Edited model comparison chart
- Edited Slides

**Jing Jin:**
- Improved Logistical Regression Model and SVM model with resampling
- Compile the master notebook codes
- Flask app setup, regex, model weights export and import
- Edited Slides, model comparison chart
- Managed Readme
- Managed Github branches

**Steven Walk:**
- Edited Slides
- Application content creation
- Proofread Readme

**Shaun Wang:**
- Front-end HTML/CSS design, development and deployment
- Flask app development and deployment
- Managed Github branches / folder structures
- Added resources to Slides
- Managed Readme




