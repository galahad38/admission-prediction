import pickle
from sklearn.linear_model import LogisticRegression
import gradio as gr
import numpy as np

with open('logreg_model.pkl', "rb") as file:
    loaded_model = pickle.load(file)

with open('scaler.pkl', 'rb') as file2:
    loaded_scaler = pickle.load(file2)
    
def predict_admission(gre_score, toefl_score, university_rating, sop, lor, cgpa, research, threshold=0.5):
    # Convert 'Yes'/'No' to 1/0 for the 'Research' field
    research = 1 if research == "Yes" else 0

    # Scale the new input data:
    input_data = loaded_scaler.transform([[gre_score, toefl_score, university_rating, sop, lor, cgpa]])

    # Create an input array from the provided values
    input_data = [np.append(np.append(np.array([[1.]]),input_data),research)]  # Added a 1 for the intercept and research

    # Make a prediction
    prediction_probability = loaded_model.predict(input_data)[0]
    prediction = 'Admit' if prediction_probability >= threshold else 'No Admit'

    # Custom formatting for output
    prediction_color = "green" if prediction == 'Admit' else "red"
    result = f"<div style='font-size: 24px; color: {prediction_color}; font-weight: bold; font-family: Arial Black;'>Admission Prediction: {prediction}</div>"
    result += f"<br>Probability: {prediction_probability:.2f}"
    result += f"<br>Threshold Used: {threshold}"

    return result

# Define the Gradio interface
iface = gr.Interface(
    fn=predict_admission,
    inputs=[
        gr.Number(minimum=260, maximum=340, label="GRE Score"),  # Set maximum GRE score
        gr.Number(minimum=0, maximum=120, label="TOEFL Score"),
        gr.Slider(minimum=1, maximum=5, step=1, label="University Rating"),
        gr.Slider(minimum=1, maximum=5, step=0.5, label="SOP"),
        gr.Slider(minimum=1, maximum=5, step=0.5, label="LOR"),
        gr.Number(minimum=0, maximum=10, label="CGPA"),
        gr.Radio(choices=["Yes", "No"], label="Research", value="No"),
        gr.Slider(minimum=0, maximum=1, step=0.01, value=0.5, label="Threshold")
    ],
    outputs=gr.HTML(label="Prediction"),
    allow_flagging="never"
)

iface.launch()