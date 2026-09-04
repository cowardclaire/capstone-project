# Retail Sales Analytics & Prediction Dashboard

## Project Overview

With this project I have been aiming to understand what product attributes impact sales volume. My dataset had many different ones such as product categories, price, product position in store, promotional activity etc. I wanted to know which ones had the biggest impact so I could create a model that could forecast how many units we could sell depending on the different attributes – expecting this to vary depending on each one.

I analysed the retail products performance looking at pricing behaviour, promotional impact, and category trends. I’ve used EDA (exploratory data analysis), pulling different visuals to help me better understand the data, machine learning modelling to predict sales volume, as well as an interactive Streamlit dashboard to help a retail team make data driven forecasts.

The dashboard allows users to:

•	Understand the correlations between product pricing, category trends, and promotional activity on sales volume
•	Review insights and recommendations
•	Predict sales volume using the model

## Business Model

This project aims to help retailers understand what drives product sales, the impact of pricing and promotions. Which categories perform best, and help manage stock levels through better forecasting.
,

## Project Structure
*used copilot to create below project structure tree

capstone-project/
├── data/                     # Raw and cleaned datasets
├── visuals/                  # EDA charts and plots
│   └── eda/
├── src/                      # Model training scripts
├── jupyter_notebooks/        # Full EDA + modelling notebook
├── streamlit_app/            # Dashboard application
│   ├── Main_Page.py          # Home page
│   └── Pages/
│       ├── EDA.py
│       ├── Model_Predictions.py
│       └── Insights_and_Recommendations.py
└── README.md                 # Project documentation

## How to run the Dashboard
### Create and activate the virtual environment (if not already live) :
- python -m venv .venv
.venv\Scripts\activate

### Install requirements :
pip install -r requirements.txt

### Run the Streamlit application – 
First go into the Main Page which is the root of streamlit app:
capstone-project/
│
├── streamlit_app/            # Dashboard application
│   ├── Main_Page.py          # Home page

And paste into the terminal – “streamlit run streamlit_app/Main_Page.py”

This will open a browser, taking you to the web page for the Retail Dashboard.

## Dashboard Pages

Main Page – introducing the dashboard
EDA – shows my key visuals 
Insights & Predictions – explains my findings of which attributes have the biggest impact on sales, and how businesses could use the model to improve their sales and stock position
Model Predictions – allows users to toggle with pricing, promotion, store position, and product categories before predicting sales volume

## Model Overview

I consulted AI to help me choose which model would be best for my dataset and what I set out to achieve with this project. 

It guided me to use the XGBoost Regressor as it captures patterns by making lots of decision trees and combines them to make predictions. Instead of forcing a straight line through my data like linear regression would, XGBoost builds flexible rules that suits retails varying behaviours.

This model uses feature engineering such as OHE (one hot encoding), as well as train/test split	, and used RMSE and R² to evaluate.

After creating the model, I consulted AI to help me with saving the model so that it was reusable. It advised and guided me to save as a pkl file which allows me to load the model inside my Streamlit app and make predictions instantly. I didn’t want to have to train and test every time the dashboard runs.

## Key Findings

•	Price has a strong impact on sales volume
•	Promotions significantly increase demand
•	Categories sell averagely similar volumes
•	Position in store didn't impact volumes until on promotion
•	The model predicts sales volume with strong accuracy

## Conclusion

Overall this project has looked at retail sale volume, finding out what really drives performance. I explored the different product attributes, and found that price was the biggest driver, shown through the biggest correlation between sales volume and promotion. After exploring the dataset through visuals, I created a model that would forecast sales based on attributes such as if on promotion, what category the product fell into, store position and price. Then I created a simple Streamlit dashboard that allowed users to toggle between these features before forecasting the units they would sell. 
Through this project I worked through the full data analytics cycle from cleaning the raw data, through to EDA and insights, to creating a model as well as a Streamlit dashboard. It shows how data can help with commercial decisions backed by data.
