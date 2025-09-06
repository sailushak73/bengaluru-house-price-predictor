
# Bengaluru House Price Predictor

This is a machine learning project that predicts house prices in Bengaluru based on features like area (sq ft), number of bedrooms (BHK), bathrooms, balconies, etc. The dataset is cleaned and preprocessed before training a regression model using scikit-learn.

The trained model is saved using Python’s pickle module and deployed as an interactive web application using Streamlit. Users can input property details through the web interface and get real-time price predictions.

## Features
- Data cleaning and preprocessing with Pandas
- Machine learning model built with scikit-learn
- Model saved using pickle for reuse
- User-friendly interface built with Streamlit
- Instant price prediction based on user inputs

## How to Use
1. Clone the repository  
2. Install the required Python libraries listed in `requirements.txt`  
3. Run the Streamlit app with:  
   ```bash
   streamlit run app.py
4.Enter property details and see the predicted price!

Technologies Used :
Python
Pandas, NumPy
scikit-learn
Streamlit
Git & GitHub for version control
