# DigitalSys-Assessment
Repository created for the assessment task for the Django Consultant position


## Features
- Create a loan application via the web using a simple form created in React.
- As an admin, you can view all loan applications and change their status from ```Manual Validation``` only to ```Approved``` or ```Denied```.
- As an admin, you can define what type of information is required from the user to send to the form.


## Requirements
Ensure a seamless setup with the following prerequisites:

- Docker - [Install guide](https://docs.docker.com/get-docker/)
- To access the Admin Panel, you will need the following username and password:
username: ```admin```, password: ```test```.

## Setup
1. Clone github repository in your local system ```git clone https://github.com/FelippoDev/DigitalSys-Assessment```
2. Navigate to the project directory in your terminal
3. Create the necessary environment variables: locate the file ```.env.example``` within the repository, renamed the ```.env.example``` to ```.env```.
4. At last, run the ```command docker-compose up --build```

## Starting
You can access the loan form and admin panel by visiting this URL in your preferred browser.
React form: ```http://127.0.0.1:5173/```
Admin Panel: ```http://127.0.0.1:8000/admin/``` username: ```admin``` password: ```test```


## Web App
The frontend was developed using react, CSS and HTML. The web part is basically a form where the user can apply for his loan. Once the user submits their application, a pop-up message notifies them that their request has been sent.

All the fields can be removed from the form, besides the fields: ```Número de Documento``` and ```Valor```, for seeing how the admin does that check in the [Admin Panel](##Admin) section below. React will be informed of the necessary fields from the user via a backend endpoint that returns all customizable fields.


## API

In the Backend we have 2 endpoints:
- ```http://127.0.0.1:8000/api/v1/loan``` endpoint for creating a loan proposal, in this APIView, after success, sends a response informing the fields that were created within initial status of the loan proposal set to ```pending``` . Additionally, it initiates an async task with celery to verify with an external API if the user's loan proposal can receive approval or not, based on the response received. If the response returns False it will set the status of the proposal has ```Denied``` else ```Manual Validation```.

- ```http://127.0.0.1:8000/api/v1/proposal-fields``` Endpoint to which the React application sends a request to determine the necessary fields for the form, among thoses customizable fields.


## Admin
In the admin panel you have 2 main features, In the Loan Category:
- In ```Loan proposals```, you will find a list containing all loan applications made by users, and you can freely update the fields, except for the ```status``` field. The status field can only be updated when it's set as ```Manual Validation```. This status is assigned when the request made in the external API inside the asynchronous task returns ```True```. If this is not the case, the admin cannot update the ```status``` field in the admin panel.

- In ```Proposal fields configuration```, You will find all the fields available in the Loan Proposals model, that can be customed, which can be customized by marking the checkbox to indicate whether they are required or not. 
Please note that marking a field as required or not will impact the entire API and the React form. Your decision will determine whether the field is essential for creating a loan proposal.


