
// /ethereum/smart_contracts/ComplianceContract.sol
// Author: Jacob Thomas Messer Redmond
// UUID: UUID-00101010114

pragma solidity ^0.8.0;

contract ComplianceContract {
    address public owner;
    mapping(address => bool) public compliantAddresses;

    event ComplianceStatusChanged(address indexed account, bool status);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    function setComplianceStatus(address account, bool status) public onlyOwner {
        compliantAddresses[account] = status;
        emit ComplianceStatusChanged(account, status);
    }

    function checkCompliance(address account) public view returns (bool) {
        return compliantAddresses[account];
    }
}
