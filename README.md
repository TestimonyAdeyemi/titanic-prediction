# Titanic Survival Prediction

This GitHub repository contains a Streamlit web application for predicting Titanic survival based on selected features. The application loads a pre-trained machine learning model and allows users to input their gender, passenger class, number of siblings/spouses, and number of parents/children. After providing the inputs, users can click the "Predict Survival" button to get the model's prediction.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python 3.x
- Streamlit
- scikit-learn
- Pillow (PIL)

Install the required packages using the following command:

```bash
pip install streamlit scikit-learn Pillow
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/titanic-survival-prediction.git
cd titanic-survival-prediction
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. Access the app in your web browser at `https://titanic-prediction-enoaqugptvg3ikdutexxvv.streamlit.app/`.

## Application Features

- **User Input:** Select your gender, passenger class, and provide the number of siblings/spouses and parents/children.
- **Prediction:** Click the "Predict Survival" button to see the model's prediction.
- **Result Display:** The app displays a success message if the prediction indicates survival and an error message otherwise.
- **Image Display:** Accompanying images are shown based on the prediction result.

## Note

- The application utilizes Streamlit for the web interface.
- The machine learning model (`titanic_model.pkl`) is pre-trained and loaded from a saved file.
- The displayed images are loaded based on the prediction result.

Feel free to customize the application further based on your needs. If you encounter any issues or have suggestions for improvement, please create an issue in the GitHub repository.
