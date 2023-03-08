# Repository for Ravi's Project3 submission.

## Project Name: "Distributed Account Verification System - DAVS" 
>> provides a real-time 'Bank Account Verification' service

The aim of my project is to create a dApp that provides a real-time 'Bank Account Verification' service. 

The demand for such a Bank Account Verification service is fairly common in the Banking/Payments world - essentially it's a request from a Payor to check whether the Payee bank account is valid; the Payee bank would confirm whether the bank account is: (a) Open/Closed or (b) has Incorrect Account Number or (c) has Incorrect Account/Bene Name, etc.

However the experience currently for clients globally is very fragmented. In countries such as South Korea, it is a regulatory requirement for banks to provide this service and hence is quite prevalent there. In the US, this is a requirements for NACHA 'Web Debit Rule' compliance, however in most other countries no such service exists though the benefits are significant (fraud prevention, improve STP/less chances of delayed payments, etc) and the demand for such a service exists. Deploying this solution on a blockchain takes away the current geographical and technology complexities that limit the availability of a standardized, global service.

The idea is to connect all stakeholders engaged in the Money movement/Payments world (i.e., banks, non-bank fintechs, Credit Unions, Money Transfer services, Digital Banks, Corporates, etc) in a global, decentralized, private and permissioned blockchain. Participants can query the blockchain (the data in each block will have a dictionary that stores details such as the Bank Name, Branch Name, Account Number, Account Name and Account Status) and receive a response. For the purpose of this project, we will limit the service to only 'validating' the Bank Account Status i.e. the service will only provide a simple 'Account Open/Account Closed' response. The service can be expanded in later projects to respond with correct values (e.g., in case of incorrect or incomplete account numbers or names in query requests) or even provide activity status (e.g., whether there was any transaction activity in the account in past 30/60/90 days).

Among the large global banks, J.P. Morgan has a similar blockchain-based service called 'Confirm':
https://www.jpmorgan.com/solutions/treasury-payments/insights/validate-account-information-with-confirm

The following elements will be used in the project:
- All data will be provided by the participants and will be stored in a Ethereum blockchain (only 5 data elements are required for now: Bank Name, Branch Name, Account Number, Account Name and Account Status)
- All User Interface screens (for Data Upload and Data Query) will be built using Streamlit, and will be responded automatically by a Smart Contract developed in Solidity.
- The Remix IDE will be used for the Solidity development and Python/Streamlit for the main program and UI.
- EthereumTesterProvider be leveraged to test the functionality of the above mentioned functionality.
