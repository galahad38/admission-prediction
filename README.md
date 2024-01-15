# Admission Prediction

## What it does:

A classification model that predicts whether or not an MS application will be accepted or rejected by a University.

This project was built to test my understanding of deploying a Machine Learning Model as a simple Web app on [HuggingFace](https://huggingface.co/spaces/gsubr/admission-prediction) as part of the PGP-DSE program at Great Learning Hyderabad.

The code used to build the model itself is irrelevant for this project, as the objective was to take a pickled model, read it, and put together a Web app for users to interact with and obtain predictions from the model. Enter the required details, Click 'Submit', and obtain the prediction given by the classification model.

## How to build it yourself:

1. Install [Python](https://www.python.org/downloads/).
2. Download [requirements.txt](https://github.com/galahad38/admission-prediction/blob/main/requirements.txt).
3. Install non-standard Python libraries:
     launch command prompt in the folder containing requirements.txt and run this command:
     ```console
     C:\Windows\system32\ pip install -r requirements.txt
     ```
4. Download [app.py](https://github.com/galahad38/admission-prediction/blob/main/app.py).
5. Run the python script:
     launch command prompt in the folder containing app.py and run this command:
     ```console
     C:\Windows\system32\ python app.py
     ```
6. Alternatively, launch app.py on your IDE of choice.
7. If it doesn't launch on its own, click on the IP address that appears.
8. Profit!

## How to use it:

Enter the following details into the Gradio Interface:

* GRE Score: The applicant's GRE Score. Ranges from 260 to 340. 
* TOEFL Score: The applicant's TOFEL Score. Ranges from 0 to 120.
* University Rating: How good the University is. Integer values ranging from 1 to 5.
* SOP: Strength of the applicant's Statement of Purpose. Ranges from 0 to 5, with a step size of 0.5
* LOR: Strength of the applicant's Letter of Recommendation. Ranges from 0 to 5, with a step size of 0.5
* CGPA: The applicant's Cumulative Grade Point Average obtained during their Undergrad. Float values ranging from 0 to 10.
* Research: Whether or not the applicant has Research Experience. Yes/No
* Threshold: Value that determines at what point the prediction is 'Accepted'. Feel free to play around with this value, or leave at it at its default.

Click on 'Submit' to obtain the prediction made by the classification model on the backend.

## How to interpret it:

'Admission Prediction: Admit' - The applicant will be accepted by the University for their MS program.

'Admission Prediction: No Admit' - The applicant will be rejected by the University for their MS program.

## Future Scope:

I am satisfied with the outcome of this project. However it is simplistic and undoubtedly a prototype with huge scope for improvement:
1) The model itself can be improved, by using a more complex algorithm.
2) The HuggingFace Space can be linked to this GitHub Repo, so that any changes committed to the repo are synced with the Space.
