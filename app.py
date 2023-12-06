import streamlit as st
import numpy as np
import librosa
import joblib

# Load the trained model
@st.cache(allow_output_mutation=True)
def load_model():
    # Replace 'RandomForestClassifier()' with the actual instantiation of your model class
    return joblib.load('G:\\DataScience Project\\Machine Learning\\parkinson _diesease_detection_by_voicedata\\random_forest_parkinson_model.pkl')


model = load_model()

# Streamlit app
st.title('Parkinson Disease Detection App')

# User input for testing
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

# Function to extract voice features
def extract_voice_features(audio_file):
    # Use librosa to extract voice features (example with MFCCs)
    y, sr = librosa.load(audio_file)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=8)
    return np.mean(mfccs, axis=1)

if uploaded_file is not None:
    # Extract voice features from the uploaded audio file
    voice_features = extract_voice_features(uploaded_file)
    
    # Display the extracted features
    st.write('Extracted Voice Features:')
    st.write(voice_features)

    # Convert the features to a numpy array
    user_input = np.array(voice_features).reshape(1, -1)

    # Make prediction
    if st.button('Predict'):
        prediction = model.predict(user_input)
        st.write('Prediction Result:')
        st.write(f'The predicted class is: {prediction[0]}')
    
