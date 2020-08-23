import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import streamlit as st
from sklearn.metrics import mean_squared_error, r2_score

customers = pd.read_csv('data/Ecommerce Customers.csv')
customers.dropna(axis = 1)
customers = customers.drop(['Email', 'Address', 'Avatar'], axis = 1)

st.title("Welcome to the app to predict amount yearly spent by Customers on this E-Commerce Clothing Website")

st.write("This is an application for viewing the difference in revenue between the company's app and website, and revenue generated by company through their platforms.")
check_data = st.checkbox("See the sample data")
if check_data:
    st.write(customers.head())
st.write("Now let's find out how much the amount spent when we choose some parameters.")

#input the numbers
avg_session_length = st.slider("Average session length?:",int(customers['Avg. Session Length'].min()),int(customers['Avg. Session Length'].max()),int(customers['Avg. Session Length'].mean()) )
time_on_app  = st.slider("Average time on app.",int(customers['Time on App'].min()),int(customers['Time on App'].max()),int(customers['Time on App'].mean()) )
time_on_web  = st.slider("Average time on website.",int(customers['Time on Website'].min()),int(customers['Time on Website'].max()),int(customers['Time on Website'].mean()) )
length_of_member = st.slider("Length of User Membership",int(customers['Length of Membership'].min()),int(customers['Length of Membership'].max()),int(customers['Length of Membership'].mean()) )

X = customers.drop('Yearly Amount Spent', axis = 1)
y = customers['Yearly Amount Spent']

# Splitting data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=101)

# Creating model
lm = LinearRegression()

# Fitting model
lm.fit(X_train, y_train)
lm.predict(X_test)

errors = np.sqrt(mean_squared_error(y_test,lm.predict(X_test)))

predictions = lm.predict([[avg_session_length,time_on_app,time_on_web,length_of_member]])[0]

sns.regplot(y_test, lm.predict(X_test))
plt.xlabel('Yearly Amount Spent given training data')
plt.ylabel('Predicted yearly amount spent on test data')
st.pyplot()

if st.button("Click me to get results!"):
    st.header("Yearly amount spent on platform is predicted to be USD {}".format(int(predictions)))
    st.subheader("Your range of prediction of yearly amount spent is USD {} - USD {}".format(int(predictions-errors),int(predictions+errors) ))




