# FakeDataSet_RetailFinancial

README
This document aims to provide a detailed understanding of the approach used to generate a fake dataset. It will explain the different components of the code and any assumptions that were made.
Dataset Overview
The generated dataset contains data for 100 clients, with 730 snapshots for each client, covering a period of two years from January 1, 2021. The dataset comprises four categories of data: Sociological Features, Financial Features, Communicational Features, and Loan Features.
Assumptions
Before starting the development of the code, several assumptions were made:
	1.	The start date to generate data is January 1, 2021, with random values assigned for each customer on day one.
	2.	The data will be generated for 100 clients and 730 snapshots (365 days * 2 years).
Approach
The code for generating the fake dataset has been designed with the following approaches in mind:
	1.	Design patterns and object-oriented programming (OOP) were used to create an extensible and easy-to-read code structure.
	2.	User-centered methodology was employed to ensure the code was understandable to the user.
	3.	The code was designed with the intention of being coherent over time. Therefore, the code was structured in a way that future developers can easily understand and modify it.
	4.	Error handling was an important aspect of the code. The code has been written to detect and handle errors whenever possible.
Design and Implementation
The code consists of four classes: SociologicalFeatures, Loan, FinancialFeatures, and CommunicationalFeatures.
SociologicalFeatures
This class stores the sociological features of a customer. It takes in the following attributes:
	•	Customer ID
	•	Birth year
	•	Geography
	•	Marital status
	•	Employment status
	•	Gender
	•	Education level
	•	Date
	•	Area
	•	Insured
The class also calculates the age of the customer based on their birth year. The class has two methods, update_date and calculate_age, which update the date and calculate the customer's age, respectively.
Loan
The Loan class is used to store loan features of a customer. It takes in the following attributes:
	•	Loan ID
	•	Customer ID
	•	Date
	•	Amount
	•	Loan Type
The class allows the customer to make payments on the loan through the make_repayment method.
FinancialFeatures
The FinancialFeatures class stores the financial features of a customer. It takes in the following attributes:
	•	Customer ID
	•	Date
	•	Current balance
	•	Current debt
	•	Credit score
	•	Loan amount
	•	Loan repayment
	•	Savings
	•	Investment
	•	Loan type
The class has a current_balance property which allows the current balance of the customer to be accessed and updated.
CommunicationalFeatures
The CommunicationalFeatures class stores the communication features of a customer. It takes in the following attributes:
	•	Customer ID
	•	Date
	•	Calls to branch
	•	Visits to branch
	•	Mobile entrances
	•	Online entrances
	•	ATM withdrawals
	•	ATM deposits
	•	Emails sent
	•	SMS sent
	•	Letters sent
generate_fake_dataset Function
The generate_fake_dataset function is responsible for creating a fake dataset for the four classes mentioned above. The function takes in two arguments, num_clients and num_days. It generates random data for each client and each day for a period of num_days.
Data Gathered
The data was gathered using Python's built-in random module, which provides a simple way of generating random data. The dataset was generated using the generate_fake_dataset function, which creates random data for each category of features for each customer.

Variables 
Sociological Features:
	•	Customer ID: unique identifier for each customer
	•	Birth year: the year the customer was born
	•	Geography: the country or region the customer lives in
	•	Marital status: the marital status of the customer (e.g. single, married, divorced)
	•	Employment status: the current employment status of the customer (e.g. employed, unemployed, student)
	•	Gender: the gender of the customer
	•	Education level: the highest level of education completed by the customer
	•	Date: the date of the snapshot
	•	Area: the customer's residential area
	•	Insured: whether the customer has insurance or not

Loan Features:
	•	Loan ID: unique identifier for each loan
	•	Customer ID: the customer ID associated with the loan
	•	Date: the date of the loan snapshot
	•	Amount: the total amount of the loan
	•	Loan Type: the type of loan (e.g. personal loan, mortgage)

Financial Features:
	•	Customer ID: unique identifier for each customer
	•	Date: the date of the snapshot
	•	Current balance: the current balance of the customer's account
	•	Current debt: the current debt of the customer
	•	Credit score: the customer's credit score
	•	Loan amount: the total amount of the loan
	•	Loan repayment: the amount of the loan repayment
	•	Savings: the amount of the customer's savings
	•	Investment: the amount of the customer's investment
	•	Loan type: the type of loan (e.g. personal loan, mortgage)

Communicational Features:
	•	Customer ID: unique identifier for each customer
	•	Date: the date of the snapshot
	•	Calls to branch: the number of times the customer called the branch
	•	Visits to branch: the number of times the customer visited the branch
	•	Mobile entrances: the number of times the customer used mobile banking
	•	Online entrances: the number of times the customer used online banking
	•	ATM withdrawals: the number of times the customer withdrew money from an ATM
	•	ATM deposits: the number of times the customer deposited money at an ATM
	•	Emails sent: the number of emails sent by the customer
	•	SMS sent: the number of SMS messages sent by the customer
	•	Letters sent: the number of letters sent by the customer

