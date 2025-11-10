# Iris Classifier Web App 
![Alt text](https://github.com/Joy-analyst/Iris-classification/blob/main/Screenshot%202025-11-10%20081429.png)



This project is a Streamlit web application that predicts the species of an Iris flower based on user-provided sepal and petal measurements. The goal was to build an interactive interface that allows anyone to input values and receive an instant prediction using a trained machine learning model.

The project was developed using Python in VS Code, with Anaconda used to manage the environment and packages. The workflow involved loading and cleaning the Iris dataset, exploring the data, training a Decision Tree Classifier, evaluating model performance, and finally creating a web app with Streamlit for real-time predictions.

Data cleaning steps included checking for missing values, verifying data types, and ensuring no duplicates were present. Exploratory data analysis helped identify patterns and relationships between features and the target variable. Features used in the model were sepal length, sepal width, petal length, and petal width.

The model was trained using scikit-learn, and the trained model was saved with `joblib`. Model evaluation showed an accuracy of approximately 97% on the test dataset, demonstrating that the classifier can reliably predict the Iris species. The prediction code was written to allow both individual row predictions from Jupyter Notebook and interactive user input through the Streamlit app.

The Streamlit app was run locally using the command `streamlit run app.py` in Anaconda Prompt or VS Code terminal, displaying an interactive interface where users can input feature values and receive predictions instantly. 
The app can also be deployed online, and you can access the live version [here](https://iris-classification-cm26lvidosswt9dk8cghmh.streamlit.app/).

---

## Key Features and Findings

- Data cleaning and preprocessing ensured reliable input for the model.
- Exploratory data analysis highlighted correlations between features and target species.
- The Decision Tree Classifier achieved high accuracy (~97%) in predicting Iris species.
- Users can input flower measurements via a web interface and receive real-time predictions.
- The app demonstrates an end-to-end machine learning workflow: from dataset preprocessing to model deployment.

---

## Technologies Used

Python 3.12, VS Code, Anaconda, Streamlit, pandas, scikit-learn, joblib, Jupyter Notebook

---

## Contact

- **Email:** joyuko22@gmail.com  
- **LinkedIn:** [linkedin.com/in/joy-uko](https://linkedin.com/in/joy-uko)  
- **GitHub:** [github.com/joyuko](https://github.com/joy-analyst)
