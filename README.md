
# Retail Sales Analytics & Prediction Dashboard

## Project Overview

With this project, I have been aiming to understand which product attributes impact sales volume. My dataset had many different variables, such as product categories, price, product position in store, and promotional activity. I wanted to know which ones had the biggest impact so I could create a model that could forecast how many units we could sell depending on the different attributes, expecting this to vary depending on each one.

I analysed retail product performance by looking at pricing behaviour, promotional impact, and category trends. I’ve used EDA (exploratory data analysis), pulling different visuals to help me better understand the data, machine learning modelling to predict sales volume, and an interactive Streamlit dashboard to help a retail team make data-driven forecasts.

The dashboard allows users to:

```text
• Understand the correlations between product pricing, category trends, and promotional activity on sales volume
• Review insights and recommendations
• Predict sales volume using the model
```

## Project Purpose
This project was meant to help retailers understand what drives sales volume and to build a tool that helps forecast sales units. The purpose was to provide a data-driven dashboard that would support decision-making on pricing, promotion, and stock planning.

## Business Model

This project aims to help retailers understand what drives product sales, the impact of pricing and promotions, which categories perform best, and how to manage stock levels through better forecasting.

## Hypotheses

My initial thoughts, before EDA, were that the different attributes would increase sales, such as price, store product position, whether a product was on promotion or not, and whether there were categories that sold more than others.

I then used the EDA process to try and find out whether these were true. Looking at sales volume by category and position in store showed minimal variance, so I could draw the conclusion that neither of these were drivers of volume. From the correlation heatmap, I was able to see that the biggest driver was promotion — there was a high 0.89 correlation between promotion and sales volume. This was further confirmed when I looked at the sales volume distribution visual, where I could see two peaks indicating sales on promotion versus not on promotion. Sales volume by promotion also shows higher sales volumes when products are promoted. Product position in store showed minimal variance; however, when on promotion, I found that it did change.

## Methodology

I followed the data analytics workflow, detailed below:

#### Data Collection
I found my dataset on Kaggle.

#### Project Setup
I used the template given for this project before consulting AI for help in setting up my project structure. I knew that the layout would be important to the project and wanted to ensure from the beginning that I had a clear structure and folders.

#### Data Cleaning
I worked through cleaning the data using the steps below:

```text
• Inspecting data
• Standardising column names
• Reviewing duplicates and removing them
• Outlier detection using the IQR method
• Engineered a new feature column, bucketing sales into low, average, and high
• Used OHE to turn categorical columns into numerical values for future modelling
```

#### EDA
After cleaning and saving the data, I began exploring it using visuals. In my visualisations file, I explored:

```text
• Correlations
• Category trends
• Price behaviour
• Promotional impact
```

#### Model Selection
I consulted AI to figure out which model would be best to use with this dataset and to create a tool that could forecast sales volume.

This resulted in the choice of XGBoost Regressor because it works best with non-linear relationships, can handle categorical encoding, and has strong performance on retail data.

#### Model Evaluation
To evaluate the success of the model, I used RMSE and R².

#### Dashboard
To build my Streamlit dashboard, I consulted AI quite heavily for help on setting it up because this was an area I did not feel confident in.

AI helped set up the folder structure and write the code for each page.

## Data Management
As discussed previously, I consulted AI to help me ensure I set up my project structure in the most effective way.

Project structure below:

### Project Structure
*Used Copilot to create the project structure tree below.*

```text
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
```

## How to run the Dashboard
### Create and activate the virtual environment (if not already live):
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Install requirements:
```bash
pip install -r requirements.txt
```

### Run the Streamlit application
First, go into the Main Page, which is the root of the Streamlit app:

```text
capstone-project/
│
├── streamlit_app/            # Dashboard application
│   ├── Main_Page.py          # Home page
```

Then paste the following into the terminal:

```bash
streamlit run streamlit_app/app.py
```

This will open a browser and take you to the web page for the Retail Dashboard.

## Dashboard Pages

```text
Main Page – introducing the dashboard
EDA – shows my key visuals
Insights & Predictions – explains my findings on which attributes have the biggest impact on sales and how businesses could use the model to improve their sales and stock position
Model Predictions – allows users to adjust pricing, promotion, store position, and product categories before predicting sales volume
```

## Model Overview

I consulted AI to help me choose which model would be best for my dataset and what I set out to achieve with this project.

It guided me to use the XGBoost Regressor, as it captures patterns by making lots of decision trees and combining them to make predictions. Instead of forcing a straight line through my data like linear regression would, XGBoost builds flexible rules that suit retail’s varying behaviours.

This model uses feature engineering such as OHE (one hot encoding), as well as train/test split, and used RMSE and R² to evaluate.

After creating the model, I consulted AI to help me save it so that it was reusable. It advised and guided me to save it as a .pkl file, which allows me to load the model inside my Streamlit app and make predictions instantly. I didn’t want to have to train and test every time the dashboard runs.

## Key Findings

```text
• Price has a strong impact on sales volume
• Promotions significantly increase demand
• Categories sell similarly on average
• Position in store didn’t impact volume until promotion was applied
• The model predicts sales volume with strong accuracy
```

## Ethical Considerations, Privacy & Governance

### Ethical Considerations
The dataset used in this project is at product level and has no personal information. There are still ethical considerations to apply, such as considering bias in the predictive model. The model created was intended to support decision-making rather than replace human decisions.

### Data Privacy
The dataset does not include any customer information or personal data, which aligns with GDPR principles. Data is stored in a clear project structure with clear separation between raw and clean data.

### Data Governance
I have saved all data (raw, cleaned, and model files) in dedicated folders to ensure clear data lineage. Version control (committing to GitHub) has been done throughout to track changes to code and data processing steps. The trained model is saved as a .pkl file after consulting AI so it can be reused and easily accessed.

## Limitations, Alternative Approaches & Models

### Limitations
In terms of limitations to this project, a few are worth considering:

```text
• No time component — the data doesn’t reference any sort of time component such as day of week or time of day
• No store-level information — if this were to be used for a multi-store retailer, this model is not built to manage more than one store
• Limited product categories — only a couple are in this dataset, again meaning that if a bigger retailer with multiple product categories were involved, the model may struggle
```

### Alternative Approaches
Other approaches I could have used are listed below:

```text
Time series forecasting — a model that could predict daily, weekly, and weekend trends to better understand seasonal patterns, holiday spikes, and differences in behaviour during the week versus the weekend.

Price elasticity — a model that investigates how sensitive sales volume is to price. It could analyse how much demand drops or increases based on price.

Multi-store modelling — this could look at predicting how much a store could sell, not just a product. It would need further detail such as store size, average customers, and average spend, but it could have been an interesting project.
```

### Alternative Models
When I consulted AI to help me understand which model was best for my project, it also considered Random Forest and LightGBM.

#### Random Forest vs XGBoost
Random Forest was described as great for simpler tabular data, reducing overfitting and delivering quick baselines. However, compared with XGBoost, it struggles with more complex interactions such as price versus promotion and does not learn sequentially. XGBoost builds upon each tree, correcting mistakes as it goes and is strong at capturing promotional uplift more accurately.

#### LightGBM vs XGBoost
LightGBM was described as great for huge datasets and uses leaf growth methods. In terms of weaknesses, it is known to overfit, require more tuning, and can struggle with OHE features. Whereas XGBoost is more stable, predictable, and easier to tune, and my dataset was not large enough for LightGBM.

## Future Improvements
Looking ahead, this project could continue to grow by adding seasonality and holiday effects such as Christmas, Black Friday, and Easter. While we can currently forecast sales volume and see how much promotion drives this, the next logical step would be to add margins. To further delve into profitability, it would be useful to know each product’s margin so we could create a model that suggests what depth of promotion would drive more sales volume while protecting profitability.

## Version Control
I used GitHub for version control, committing once I had made big, meaningful changes. I received feedback from my course tutor that I needed to be committing more often near the beginning. I made these changes and began committing more often, which is why you can see more commits from the middle of the capstone project.

## Communication Strategy
Throughout this project, I have aimed to create visuals, insights, and a dashboard that could be used by technical and non-technical users. In retail, from my experience, there are different levels of data understanding, and so when creating the dashboard I had this in mind and made it as intuitive as possible. The insights and recommendations page was written to help explain the visuals and what the findings are so that a non-technical user could understand the information easily. While the EDA, modelling choices, and evaluation metrics provide the deeper detail a technical user would expect to see, the overall aim was to communicate the analysis in a way that was accessible to both types of users.

## Conclusion

Overall, this project has looked at retail sales volume, finding out what really drives performance. I explored the different product attributes and found that price was the biggest driver, shown through the strongest correlation between sales volume and promotion. After exploring the dataset through visuals, I created a model that would forecast sales based on attributes such as whether the product was on promotion, what category it fell into, store position, and price. Then I created a simple Streamlit dashboard that allowed users to toggle between these features before forecasting the units they would sell.

Through this project, I worked through the full data analytics cycle from cleaning the raw data, through EDA and insights, to creating a model and a Streamlit dashboard. It shows how data can help with commercial decisions backed by evidence.
