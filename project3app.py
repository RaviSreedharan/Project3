################################################################################
# Imports
import streamlit as st
from typing import Any, List

# from dataclasses import dataclass
# from datetime import datetime
# import hashlib
# import pandas as pd
# Import the Web3 library and RPC provider

from web3 import Web3, EthereumTesterProvider
import json
import os
from pathlib import Path
# from dotenv import load_dotenv

# Create an instance of Web3
w3 = Web3()

# Create an instance of the EthereumTesterProvider
httpProvider = EthereumTesterProvider()

# Update the Web3 instance to connect to the provider
w3 = Web3(httpProvider)

################################################################################
# Function to:
#  1. Load the Streamlit contract using cache
#  2. Connect to the contract using the Contract Address and ABI
################################################################################
@st.cache(allow_output_mutation=True)
def load_contract():
    # Set the contract address (this is the address of the deployed contract)
    # contract_address = os.getenv("SMART_CONTRACT_ADDRESS")
    # contract_address = "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"
    contract_address = "0xd9145CCE52D386f254917e481eB44e9943F39138"

    # Load the contract ABI
    with open(Path('./contracts/compiled_contract.json')) as f:
        contract_abi = json.load(f)
        # print(contract_abi)

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )
    return contract

# Load the contract by calling the function
contract = load_contract()

################################################################################
# User Option 1: Add to Blockchain based on user input
#
# Create a title for our application using Markdown function in Streamlit
st.markdown("# Distributed Account Validation Service (DAVS)")

# Accept User Input for adding Account details to the DAVS database/blockchain
st.markdown("### Enter Account Details to be added to the DAVS database.")
BankName = st.text_input("Enter Bank Name")
BranchName = st.text_input("Enter Branch Name")
AccountNumber = st.text_input("Enter Account Number")
AccountName = st.text_input("Enter Account Name")
AccountStatus = st.text_input("Enter Account Status")

# Create a Streamlit `button`, and pass the “Add Block” parameter to it.
if st.button("Submit New Account Details"):
    # new_block = Block(data=BankName + " " + BranchName + " " + AccountNumber + " " + AccountName + " " + AccountStatus, creator_id=42, prev_hash=prev_block_hash)
    # st.write(new_block)   - testing only
    
    # Define the data dictionary to be added to the blockchain
    data_dict = {
        'BankName': BankName,
        'BranchName': BranchName,
        'AccountNumber': AccountNumber,
        'AccountName': AccountName,
        'AccountStatus': AccountStatus
    }
    # Encode the data dictionary as bytes
    data_bytes = w3.toBytes(hexstr=w3.sha3(text=str(data_dict)).hex())
    
    # Add the data to the blockchain using the contract's addData function
    tx_hash = contract.functions.addData(data_bytes).transact({'gas': 1000000})
    
    # Wait for the transaction to be mined
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    st.markdown("---")

################################################################################
# User Option 2: Search/Validate operation - this is the core DAVS functionality
#
# Define function to search the blockchain for a specific data block based on the first four data fields and return the 'AccountStatus' value
def search_block(bank_name, branch_name, account_number, account_name):
    events = contract.events.DataAdded().getLogs(fromBlock=0, toBlock='latest')
    for event in events:
        decoded_data = json.loads(event['data'])
        if decoded_data['BankName'] == bank_name and decoded_data['BranchName'] == branch_name and decoded_data['AccountNumber'] == account_number and decoded_data['AccountName'] == account_name:
            return decoded_data['AccountStatus']
    return None

# Accept User Input for Search/Validate operation
st.markdown("### Enter Account Details to be searched/validated.")
sBankName = st.text_input("Enter Bank Name to Validate")
sBranchName = st.text_input("Enter Branch Name to Validate")
sAccountNumber = st.text_input("Enter Account Number to Validate")
sAccountName = st.text_input("Enter Account Name to Validate")

# Search based on user input
if st.button("Validate Account"):
    # new_search = sBankName + " " + sBranchName + " " + sAccountNumber + " " + sAccountName + " " 
    # st.write(new_search)   --- testing only
    st.write(search_block(sBankName, sBranchName, sAccountNumber, sAccountName))
        
#############################################################################
# AddData.sol Solidity contract - Compiled and Deployed via Remix
#
# pragma solidity ^0.5.0;
# contract BankAccount {
#     event DataAdded(bytes data);
#
#    function addData(bytes memory data) public {
#        emit DataAdded(data);
#    }
# }
#############################################################################

#############################################################################
# Compiled JSON ABI content
#
# [
#	{
#		"constant": false,
#		"inputs": [
#			{
#				"internalType": "bytes",
#				"name": "data",
#				"type": "bytes"
#			}
#		],
#		"name": "addData",
#		"outputs": [],
#		"payable": false,
#		"stateMutability": "nonpayable",
#		"type": "function"
#	},
#	{
#		"anonymous": false,
#		"inputs": [
#			{
#				"indexed": false,
#				"internalType": "bytes",
#				"name": "data",
#				"type": "bytes"
#			}
#		],
#		"name": "DataAdded",
#		"type": "event"
#	}
# ]
#############################################################################