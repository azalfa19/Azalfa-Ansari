⚕️ Multi-Class Disease Prediction System
🎯 Project Overview 

This project implements a machine learning system to provide a preliminary, multi-class diagnosis of diseases based on patient clinical features. It is built as a web-based tool to demonstrate the end-to-end application of classification algorithms and model deployment principles, aligning with the core concepts of the AI & ML curriculum.
✨ Features 

The system provides the following major functionalities (Three Major Functional Modules):

Data Input & Validation: A user-friendly interface to input 5-10 specific clinical and physiological features (e.g., age, specific lab results).

Real-time Prediction Engine: Utilizes a trained classification model (e.g., Random Forest or Neural Network) to predict the probability distribution across three or more specific disease classes.

Diagnostic Reporting: Generates a clear output showing the top predicted disease and confidence score, including a brief interpretation.

Category,Technology/Tool,Purpose
Backend & ML,Python 3.9+,Primary programming language.
Model,Scikit-learn (or TensorFlow/Keras),"For model training, evaluation, and serialization."
Data Handling,"Pandas, NumPy","Data cleaning, preprocessing, and array manipulation."
Web Framework,Flask (or Streamlit),Serving the application and hosting the prediction API.
Version Control,Git,All project history is managed here. 
🚀 Steps to Install & Run 

Follow these steps to set up and run the system locally:

1. Prerequisites
Ensure you have Python 3.9 or later and Git installed on your system.

2. Clone the Repository
git clone <your_github_repo_link>
cd Multi-Class-Disease-Prediction

3. Setup Virtual Environment
It is highly recommended to use a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use: .\venv\Scripts\activate

4. Install Dependencies
Install all necessary libraries:
pip install -r requirements.txt

5. Run the Application
Execute the main application file (assuming you use Flask or a similar structure):
python app.py

The application will typically start on http://127.0.0.1:5000/. Open this link in your browser to access the prediction interface

🔬 Instructions for Testing 

1. Model Validation Testing
To verify the model's performance on the holdout dataset:
python tests/test_model_performance.py
Expected Output: Displays the F1-Score, Accuracy, and Confusion Matrix on the test set.

2. Unit Testing
To ensure the utility functions (preprocessing, reporting generation) work correctly:
python -m unittest tests/test_preprocessing.py
Expected Output: All unit tests should pass successfully (OK).

3. Functional Testing (Manual)
Navigate to the deployed application URL.

Input a known sample data point (from the dataset) and submit.

Verify: The system should return the correct class prediction and the prediction time should be under the 2-second non-functional requirement.
