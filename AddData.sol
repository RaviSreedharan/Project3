pragma solidity ^0.5.0;

contract BankAccount {
    event DataAdded(bytes data);

    function addData(bytes memory data) public {
        emit DataAdded(data);
    }
}