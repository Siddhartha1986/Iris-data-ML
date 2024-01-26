
# Iris Data ML Model

## Overview
This project focuses on developing a machine learning model to classify species of the Iris flower. It uses the well-known Iris dataset and predicts the species based on sepal length, sepal width, petal length, and petal width.

## Dataset
The project utilizes the Iris dataset, which contains measurements of iris flowers and is commonly used for classification tasks.

## Features and Target
- **Feature Variables:** SepalLength, SepalWidth, PetalLength, PetalWidth
- **Target Variable:** Species

## Machine Learning Model
- The model is built using the **K-Nearest Neighbours (KNN)** algorithm.
- This choice of algorithm is suitable for the classification task at hand due to its effectiveness in pattern recognition.

## User Interface and Deployment
- A user interface (UI) for the model has been created using **Streamlit**. This UI provides an interactive way for users to input flower measurements and receive species predictions.
- The model, along with its UI, is deployed and accessible via the **Streamlit.io** platform.

## Project Structure
- `app.py`: Contains the Streamlit application for the UI.
- `model.py`: Script for the KNN model.
- `prediction.py`: Handles the prediction logic.
- `data`: Directory containing the dataset.
- `output_models`: Includes the trained model files.
- `requirements.txt`: Specifies all the necessary dependencies.

## Installation and Usage
- Clone this repository to your local machine.
- Install dependencies: `pip install -r requirements.txt`
- Run the application: `streamlit run app.py`

## License
This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.




#[link to the model UI](https://siddhartha1986-iris-data-ml-app-eaf2xy.streamlit.app/)
