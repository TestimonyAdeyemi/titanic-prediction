import pickle
from PIL import Image

# Load the saved model
with open('titanic_model.pkl', 'rb') as f:
    classifier = pickle.load(f)

# Use the loaded model to make predictions
def predict_survival(gender, pclass, sib_sp, parch):
    features = [gender, pclass, sib_sp, parch]
    prediction = classifier.predict([features])
    return prediction[0]

# Create the Streamlit app
import streamlit as st

st.title('Titanic Survival Prediction')

gender = st.selectbox('Gender', ['male', 'female'])
gender = 0 if gender == 'male' else 1
pclass = st.selectbox('Passenger Class', [1, 2, 3])
sib_sp = st.number_input("How many Siblings/Spouses do you have wth you", value=None, max_value=5, min_value=0, placeholder="Type a number...")
parch = st.number_input("How many Parents/Children do you have with you", value=None, max_value=5, min_value=0, placeholder="Type a number...")

if st.button('Predict Survival'):
    prediction = predict_survival(gender, pclass, sib_sp, parch)
    if prediction == 1:
        st.success('You are predicted to survive the Titanic.')
                 
        image = Image.open('rose.gif')
        st.image(image, caption='good for you...')

    else:
        st.error('You are predicted not to survive the Titanic.')
                
        image = Image.open('fancybear2.gif')
        st.image(image, caption='down you go...')

       
