# Myers Briggs Machine Learning Project

[![All Contributors](https://img.shields.io/badge/contributors-4-green.svg?style=flat-square)](#contributors-) ![Developement](https://img.shields.io/badge/progress-in%20development-orange)

## Topic and Background
Personality

*Reasons why we selected our topic:*

Myers-Briggs Type Indicator (MBTI) is one of the most prevalent personality tests in the world. Its purpose is to categorize psychological profiles based on the assumption that variations in everyday behavior are ordered, consistent, and capable of being categorized. Currently, the MBTI test is performed by an online quiz. 

However, these tests often include intrinsic biases because the subject is conscious of the quiz processes and will answer accordingly. Therefore, we wanted to create a more objective process for testing MBTI. By inputting writing from the subject, we hope to train a machine learning model to predict their personality category through text analytics. Hopefully, this will eliminate input biases from the subject.

## Data Source
The Myers-Briggs Type Indicator (MBTI) is a taxonomy that divides everyone into 16 distinct personality types across four axes: 
- Introversion (I) – Extroversion (E) 
- Intuition (N) – Sensing (S) 
- Thinking (T) – Feeling (F) 
- Judging (J) – Perceiving (P) 

The dataset contains ~8600 observations (people), where each observation gives a person’s: 
- Myers-Briggs personality type (as a 4-letter code) 
- An excerpt containing the last 50 posts on their PersonalityCafe forum (each entry separated by “|||”) 

This data was collected through the PersonalityCafe forum, as it provides a large selection of people and their MBTI personality types, as well as what they have written. 

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

## Objectives
Our objectives are divided into four segments with 4 different contributor roles:

#### Segment 1:
* Selected topic
* Reason why they selected their topic ✓ Description of their source of data
* Questions they hope to answer with the data
* README.md: Description of the communication protocols
* At least one branch for each team member
* Each team member has at least four commits from the duration of the first segment
* Takes in data in from the provisional database
* Outputs label(s) for input data
* Sample data that mimics the expected final database structure or schema
* Draft machine learning module is connected to the provisional database

#### Segment 2:
* Description of the data exploration phase of the project
* Description of the analysis phase of the project
* Some code necessary to complete the machine learning portion of the project
* Outline of the project (this may include images, but should be easy to follow and digest)
* At least one branch for each team member
* Each team member has at least four commits for the duration of the second segment (eight total commits per person)
* Description of preliminary data preprocessing
* Description of preliminary feature engineering and preliminary feature selection, including their decision- making process
* Description of how data was split into training and testing sets
* Explanation of model choice, including limitations and benefits
* Database stores static data for use during the project
* Database interfaces with the project in some format (e.g., scraping updates the database, or database connects to the model)
* Includes at least two tables (or collections, if using MongoDB)
* Includes at least one join using the database language (not including any joins in Pandas)
* Includes at least one connection string (using SQLAlchemy or PyMongo)
* Storyboard on Google Slide(s)
* Description of the tool(s) that will be used to create final dashboard
* Description of interactive element(s)

#### Segment 3:
* Technologies, languages, tools, and algorithms used throughout the project
* All code necessary to perform exploratory analysis
* Most code necessary to complete the machine learning portion of the project
* Description of the communication protocols has been removed
* Cohesive, structured outline of the project (this may include images, but should be easy to follow and digest)
* Link to Google Slides draft presentation
* At least one branch for each team member
* Each team member has at least four commits for the duration of the third segment (12 total commits per person)
* Description of data preprocessing
* Description of feature engineering and the feature selection, including their decision- making process
* Description of how data was split into training and testing sets
* Explanation of model choice, including limitations and benefits
* Explanation of changes in model choice (if changes occurred between the Segment 2 and Segment 3 deliverables)
* Description of how they have trained the model thus far, and any additional training that will take place
* Description of current accuracy score
* Images from the initial analysis
* Data (images or report) from the machine learning task
* At least one interactive element

#### Segment 4:
* Selected topic
* Reason why they selected their topic
* Description of their source of data
* Questions they hope to answer with the data
* Description of the data exploration phase of the project
* Description of the analysis phase of the project
* Technologies, languages, tools, and algorithms used throughout the project ✓ Result of analysis
* Recommendation for future analysis
* Anything the team would have done differently
* Slides are primarily images or graphics (rather than primarily text)
* Images are clear, in high-definition, and directly illustrative of subject matter
Live Presentation
* All team members present in equal proportions
* The team demonstrates interactivity of dashboard in real time
* The presentation falls within any time limits provided by instructor ✓ Submission includes speaker notes, flashcards, or a video of the presentation rehearsal
* All code necessary to perform exploratory analysis
* All code necessary to complete machine learning portion of project ✓ Any images that have been created (at least three)
* Requirements.txt file
* Cohesive, structured outline of the project (this may include images, but should be easy to follow and digest)
* Link to dashboard (or link to video of dashboard demo)
* Link to Google Slides presentation
* At least one branch for each team member
* Each team member has at least four commits for the duration of the final segment (16 total commits per person)
* Description of data preprocessing
* Description of feature engineering and the feature selection, including the team's decision-making process
* Description of how data was split into training and testing sets
* Explanation of model choice, including limitations and benefits
* Explanation of changes in model choice (if changes occurred between the Segment 2 and Segment 3 deliverables)
* Description of how model was trained (or retrained, if they are using an existing model)
* Description and explanation of model’s confusion matrix, including final accuracy score

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

## Mock Data table:

| 1 | 3 | 14 | 18 | 22 | 78 | 99 | 101 | E-I | N-S | T-F | J-P |
|---|---|----|----|----|----|----|-----|-----|-----|-----|-----|
| 0 | 0 | 0  | 0  | 0  | 0  | 0  | 0   | 1   | 0   | 1   | 1   |
| 0 | 0 | 0  | 3  | 0  | 1  | 0  | 0   | 0   | 1   | 0   | 0   |
| 1 | 0 | 2  | 0  | 0  | 0  | 3  | 2   | 1   | 0   | 1   | 1   |
| 0 | 0 | 0  | 0  | 0  | 1  | 0  | 0   | 1   | 1   | 1   | 0   |
| 0 | 0 | 0  | 1  | 0  | 2  | 0  | 0   | 0   | 1   | 0   | 1   |

