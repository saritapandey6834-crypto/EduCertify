// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EduCertify {

    struct Certificate {
        bytes32 certHash;
        address issuer;
        uint256 issueDate;
        bool    valid;
    }

    mapping(bytes32 => Certificate) private certificates;
    address public owner;
    uint256 public verificationFee = 0.001 ether;

    event CertificateIssued(bytes32 indexed certHash, address issuer, uint256 date);
    event CertificateVerified(bytes32 indexed certHash, bool result);
    event CertificateRevoked(bytes32 indexed certHash, address revokedBy);

    modifier onlyOwner() {
        require(msg.sender == owner, 'Not authorised');
        _;
    }

    constructor() { owner = msg.sender; }

    function issueCertificate(bytes32 _hash) external onlyOwner {
        require(certificates[_hash].issueDate == 0, 'Already registered');
        certificates[_hash] = Certificate(_hash, msg.sender, block.timestamp, true);
        emit CertificateIssued(_hash, msg.sender, block.timestamp);
    }

    function verifyCertificate(bytes32 _hash) external payable returns (bool) {
        require(msg.value >= verificationFee, 'Insufficient fee');
        bool result = certificates[_hash].valid;
        emit CertificateVerified(_hash, result);
        return result;
    }

    function revokeCertificate(bytes32 _hash) external onlyOwner {
        require(certificates[_hash].issueDate != 0, 'Not found');
        certificates[_hash].valid = false;
        emit CertificateRevoked(_hash, msg.sender);
    }

    function withdrawFees() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    function setVerificationFee(uint256 _fee) external onlyOwner {
        verificationFee = _fee;
    }
}
