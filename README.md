# EduCertify — Blockchain Certificate Verification

Blockchain-based academic certificate verification system built on 
Ethereum Sepolia Testnet. Uses Solidity smart contracts and Python 
Web3.py scripts to issue, verify, and revoke certificate hashes on-chain.

**Clark University | MS Finance / FinTech | 2026**  
**Team:** Sarita Pandey & Smriti Thapaliya  
**Supervisor:** Prof. Hamidreza Ahady Dolatsara

---

## How It Works
1. University hashes a certificate PDF using SHA-256
2. Hash is stored on Ethereum blockchain via smart contract
3. Employer hashes the same PDF and queries the contract
4. Contract returns VALID or INVALID instantly

---

## Project Structure
```
EduCertify/
├── contracts/EduCertify.sol        # Solidity smart contract
├── scripts/issue_certificate.py    # Issue a certificate on-chain
├── scripts/verify_certificate.py   # Verify a certificate on-chain
├── abi/EduCertify_abi.json         # Contract ABI (added after deployment)
└── README.md
```

---

## Tech Stack
- Solidity ^0.8.0
- Ethereum Sepolia Testnet
- Python 3 + Web3.py
- MetaMask
- Remix IDE

---

## Contract Address
`0x — to be updated after Sepolia deployment`

---

## Setup Instructions
1. Install Python dependencies:
```
pip install web3
```
2. Add your details to both scripts:
   - INFURA_URL
   - CONTRACT_ADDR
   - ISSUER_ADDR or VERIFIER_ADDR
   - PRIVATE_KEY

3. Run issue script:
```
python scripts/issue_certificate.py certificate.pdf
```

4. Run verify script:
```
python scripts/verify_certificate.py certificate.pdf
```

---

## License
MIT
```

6. Commit message:
```
Fix README remove extra text
