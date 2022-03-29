# Alzheimer-s-Detection-
Project Link (GitHub repository URL): https://github.com/sakshiSakshi/Alzheimer_Detection

Project Demo URL: https://alzheimerdetection.azurewebsites.net/

• This repository consists of files required to deploy a Web App that helps detect the people affected with Alzheimers disease, created with the help of Azure Machine Learing resource and deployed as a Flask app on Microsoft Azure using Azure Static web Apps.

The project helps the user to identify whether someone is suffering from Azheimers or not by simply inputting certain values like MMSE, nWVB, ASF, eTIV with the help of a Oasis database which is also available on Kaggle.

• As stated by the World Health Organization(WHO) currently there are nearly about 55 million people who are affected by Dementia. It has been found that not much has been discovered about the consequences of Dementia in India but there are currently nearly 4 million people who are affected with different forms of Dementia in India whereas nearly 44 million people are living with this condition worldwide, by using the statistical data about how certain aspects like like MMSE,nWVB,ASF,eTIV etc., affects a person the project would be able to tell if the person has Azheimers or not by entering those values. So in a way the project will also help in monitoring the likelihood of someone developing Alzheimers. The project can be extended to include other diseases predictions as well. I used Azure Machine Learning Studio >> AutoML feature to analyze the data and find the best model to predict the dimented and non-dimented group from the dataset. I have used Static Web Apps service of Azure in my project and deployed the codes source from Vs Code to Azure using Github.

# Screenshots of the working project:-
## 1) Opens an interface to enter the values.
![image](https://user-images.githubusercontent.com/60922783/160684209-347bfda1-0518-4650-ac09-1abd0b759169.png)
## 2) Enter the values and click on submit.
![image](https://user-images.githubusercontent.com/60922783/160684524-15bb61f0-f9fb-449c-b832-8392fbf34278.png)
## 3) Shows the result.
![image](https://user-images.githubusercontent.com/60922783/160684769-4e8c9e77-5a31-45f9-ba68-8696fafe2854.png)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Azure ML Studio :
Subscription Id:- f2dffe88-5a27-4d56-92a6-07f7ea641df3. <br/>
Studio web URL:https://ml.azure.com/?tid=afcc798c-f40d-485d-879d-c7e23c09fb49&wsid=/subscriptions/f2dffe88-5a27-4d56-92a6-07f7ea641df3/resourcegroups/AI-102/workspaces/Alzheimers.<br/>
Storage: alzheimers4032293388 <br/>
Key Vault:alzheimers5216268911 <br/>
## Note: Resource has been deleted after usage.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Step 1:- Setting up Azure ML studio.
![Azure ml](https://user-images.githubusercontent.com/60922783/160679467-8f71cc32-eb23-4482-bdc4-44b8fc63d5f8.PNG)
## Step 2:- Creating compute cluster.
![createing compute cluster](https://user-images.githubusercontent.com/60922783/160679594-ada1f6f0-32a6-49bc-8678-43c0c48fcbab.PNG)
## Step 3:- Creating the dataset.
![create dataset](https://user-images.githubusercontent.com/60922783/160678822-b167fedc-8826-4dc2-9182-453bff3b5925.PNG)
## step 4:- Selecting the dataset and the required features.
![selecting the dataset](https://user-images.githubusercontent.com/60922783/160679012-c92b84c5-ba1b-448e-9c35-bab2a199abdc.PNG)
## step 5:- Configuring the AutoML run.
![configure the run](https://user-images.githubusercontent.com/60922783/160680277-75190b17-497b-447c-a705-6a477a08730a.PNG)
## step 6:- Selecting tasks and settings and running.
![selecting task](https://user-images.githubusercontent.com/60922783/160680388-ceb6aec3-0142-44c6-8f5e-51e2a3deaad3.PNG)
## step 7:- AutoML run completed.
![completed automl_run](https://user-images.githubusercontent.com/60922783/160680613-3d663c08-5812-4123-ac02-901c0710ed16.PNG)
## step 8:- Predictions and explanations of the best model.
![prediction_automl](https://user-images.githubusercontent.com/60922783/160680714-aa51203e-2854-4bc4-ac16-ddabcbcf1e2e.PNG)
## step 9:- Dowmload the model for using it in the flask web app or we can also deploy it directly as a web service inside ML studio.
## step 10: Deleting all the resources after downloading the model.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Deployment as a web app using Static Web Apps
![image](https://user-images.githubusercontent.com/60922783/160685094-2214555c-f38b-470b-9a24-feb9c2241b23.png)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Technologies used:
Azure Machine Learning,
Azure Storage Account,
Azure App Service,
AI/ML,
Flask,HTML,CSS
Python,
GitHub,
