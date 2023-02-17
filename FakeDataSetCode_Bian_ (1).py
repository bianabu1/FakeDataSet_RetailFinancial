#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
from datetime import datetime, timedelta


# In[2]:


class SociologicalFeatures:
    def __init__(self, customer_id, birth_year, geography, marital_status, employment_status, gender, education_level, date, area, insured):
        self.customer_id = customer_id
        self.birth_year = birth_year
        self.geography = geography
        self.marital_status = marital_status
        self.employment_status = employment_status
        self.gender = gender
        self.education_level = education_level
        self.date = date
        self.age = self.calculate_age()
        self.area = area
        self.insured = insured
        
    def update_date(self, new_date):
        try:
            datetime.strptime(new_date, "%Y-%m-%d")
            self.date = new_date
            self.recalculate_age()
        except ValueError:
            print("Error: Invalid date format.")
    
    def calculate_age(self):
        try:
            current_age = datetime.now().year - self.birth_year 
            if current_age < 18:
                return 18
            return current_age
        except ValueError:
            print("Error: Invalid birth year.")

    def recalculate_age(self):
        self.age = self.calculate_age()


# In[3]:


class Loan:
    def __init__(self, loan_id, customer_id, date, amount, loan_type):
        if not isinstance(date, str):
             raise TypeError("Date must be a string.")
        self.loan_id = loan_id
        self.customer_id = customer_id
        self.date = date
        self.amount = amount
        self.loan_type = loan_type
        self.repayment = 0
        self.loan_repayment = random.randint(0, min(100000, self.amount))
       
    # allows the customer to make payments on the loan.
    def make_repayment(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Repayment amount must be a positive integer.")
    
        self.repayment += amount
        return self.repayment


# In[4]:


class FinancialFeatures:
    def __init__(self, customer_id, date, current_balance, current_debt, credit_score, loan_amount, loan_repayment, savings, investment, loan_type):
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        self.customer_id = customer_id
        self.date = date
        self.current_balance = current_balance
        self.current_debt = current_debt
        self.credit_score = credit_score
        self.loan_amount = loan_amount
        self.loan_repayment = loan_repayment
        self.savings = savings
        self.investment = investment
        self.loan_type = loan_type
        self.loans = []
        
    def update_date(self, date):
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        self.date = date

    # allows the current balance of the customer to be accessed and updated.
    @property
    def current_balance(self):
        return self._current_balance

    # Stored Varaible
    @current_balance.setter
    def current_balance(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise TypeError("Current balance must be a float or int")
        self._current_balance = value


# In[5]:


class CommunicationalFeatures:
    def __init__(self, customer_id, date, calls_to_branch, visits_to_branch, mobile_entrances, online_entrances, atm_withdrawals, atm_deposits, emails_sent, sms_sent, letters_sent):
            self.customer_id = customer_id
            if not isinstance(date, str):
                raise ValueError("date must be a string")
            self.date = date
            self.calls_to_branch = calls_to_branch
            self.visits_to_branch = visits_to_branch
            self.mobile_entrances = mobile_entrances
            self.online_entrances = online_entrances
            self.atm_withdrawals = atm_withdrawals
            self.atm_deposits = atm_deposits
            self.emails_sent = emails_sent
            self.sms_sent = sms_sent
            self.letters_sent = letters_sent


# In[6]:


import pandas as pd

def generate_fake_dataset(num_clients, num_days):
    loan_id = 0
    loan_list = []
    dataset = []
    loans = []

    
    
    
    # Initialize Sociological and Financial and Communicational and Loan features for each client
    sociological_features = [None] * num_clients
    financial_features = {}
    Communicational_Features = {}
    for i in range(num_clients):
        # SocialFeature_Attributes
        geography = random.choice(['North America', 'South America', 'Europe', 'Asia', 'Africa'])
        marital_status = random.choice(['Single', 'Married', 'Divorced', 'Widowed'])
        education_level = random.choice(['High school', 'College', 'University', 'Post-graduate'])
        employment_status = random.choice(['Employed', 'Unemployed', 'Self-Employed'])
        gender = random.choice(['Male', 'Female'])
        birth_year = random.randint(datetime.strptime("2021-01-01", "%Y-%m-%d").year - 80, datetime.strptime("2021-01-01", "%Y-%m-%d").year - 18)
        area = random.choice(['04', '05', '07','08'])
        insured = random.choice(['Yes', 'No'])
        # Loan and FinancialFeature_Attributes
        current_balance = random.randint(0, 1000000)
        current_debt = random.randint(0, min(100000, current_balance))
        credit_score = random.randint(400, 850)
        loan_amount = random.randint(0, min(100000, current_balance))
        loan_repayment = random.randint(0, min(100000, loan_amount))
        savings = random.randint(0, 1000000)
        investment = random.randint(0, 1000000)
        loan_type = random.choice(['Personal', 'Home', 'Car', 'Education'])
        # communicationalFeature _ Attributes
        calls_to_branch = random.randint(0, 10)
        visits_to_branch = random.randint(0, 5)
        mobile_entrances = random.randint(0, 5)
        online_entrances = random.randint(0, 5)
        atm_withdrawals = random.randint(0, min(100, current_balance))
        atm_deposits = random.randint(0, max(100, 10000))
        emails_sent = random.randint(0, 5)
        sms_sent  = random.randint(0, 5)
        letters_sent = random.randint(0, 5)

        sociological_features[i] = SociologicalFeatures(i, birth_year, geography, marital_status, employment_status, gender, education_level, "2021-01-01", area, insured)
        Communicational_Features[i] = CommunicationalFeatures(i, "2021-01-01",calls_to_branch,visits_to_branch,mobile_entrances,online_entrances,atm_withdrawals,atm_deposits,emails_sent,sms_sent,letters_sent)
        if loan_amount == 0:
            loan_type = 'Not Taken'
        else:
            loan_type
        loan = Loan(loan_id, i, "2021-01-01", loan_amount, loan_type)
        loans.append(loan)
        financial_features[i] = FinancialFeatures(i, "2021-01-01",current_balance,current_debt,credit_score,loan_amount,loan_repayment,savings,investment, loan_type)

     # update the date of each client's Sociological features and generates new random Communication features   
    for j in range(num_days):
        date = datetime.strptime("2021-01-01", "%Y-%m-%d") + timedelta(days=j)
        date = date.strftime("%Y-%m-%d")

        for i in range(num_clients):
            sociological_features[i].update_date(date)
            # communicationalFeature _ Attributes
            calls_to_branch = random.randint(0, 10)
            visits_to_branch = random.randint(0, 5)
            mobile_entrances = random.randint(0, 5)
            online_entrances = random.randint(0, 5)
            atm_withdrawals = random.randint(0, min(100, current_balance))
            atm_withdrawals = random.randint(0, min(100, current_balance))
            atm_deposits = random.randint(0, max(100, 10000))
            emails_sent = random.randint(0, 5)
            sms_sent  = random.randint(0, 5)
            letters_sent = random.randint(0, 5)
            Communicational_Features[i] = CommunicationalFeatures(i, date, calls_to_branch, visits_to_branch, mobile_entrances, online_entrances, atm_withdrawals, atm_deposits, emails_sent, sms_sent, letters_sent)
            if Communicational_Features[i].atm_withdrawals == 0 and Communicational_Features[i].atm_deposits == 0: 
                financial_features[i].update_date(date)
            else :
                financial_features[i].current_balance = financial_features[i].current_balance - Communicational_Features[i].atm_withdrawals + Communicational_Features[i].atm_deposits
            
            

            # Check if client has taken a loan in the last few days
            loan_taken = False
            for loan in loan_list:
                if loan['customer_id'] == i and (datetime.strptime(date, "%Y-%m-%d") - datetime.strptime(loan['date'], "%Y-%m-%d")).days <= 3:
                    loan_taken = True
                    break

            # Grant loan if client's current balance is sufficient and they have not taken a loan in the last few days
            if random.random() < 0.07 and financial_features[i].current_balance > 10000 and not loan_taken:
                loan_size = random.randint(min(10000, financial_features[i].current_balance), financial_features[i].current_balance)
                loan = Loan(loan_id, i, date, loan_size, loan_type)
                financial_features[i].loan_amount = loan_size
                financial_features[i].current_debt -= loan_size
                financial_features[i].current_balance += loan_size
                loan_list.append(loan.__dict__)
                loan_id += 1

            # Determine if client takes a loan the day after a snapshot
            if j + 1 < num_days:
                next_date = datetime.strptime("2021-01-01", "%Y-%m-%d") + timedelta(days=j+1)
                next_date = next_date.strftime("%Y-%m-%d")
                next_loan_taken = False
                for loan in loan_list:
                    if loan['customer_id'] == i and (datetime.strptime(next_date, "%Y-%m-%d") - datetime.strptime(loan['date'], "%Y-%m-%d")).days <= 3:
                        next_loan_taken = True
                        break
                nextloanTaken = int(next_loan_taken)

            features = {
                **sociological_features[i].__dict__,
                **financial_features[i].__dict__,
                **Communicational_Features[i].__dict__,
                "nextloanTaken": nextloanTaken
            }
            dataset.append(features)

    df = pd.DataFrame(dataset)
    return df


# In[7]:


FakeData = generate_fake_dataset(100,730)


# In[8]:


ParquetData_Bian = pd.DataFrame(FakeData).to_parquet


# In[9]:


FakeData.to_parquet('Parquet_FakeDataSet_Bian.parquet')

