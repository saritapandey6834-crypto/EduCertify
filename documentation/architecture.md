# EduCertify — System Architecture

## Four-Layer Architecture

### Layer 1 — Blockchain (Ethereum Sepolia)
- Stores certificate hashes permanently
- Executes smart contract logic
- Records all transactions immutably

### Layer 2 — Smart Contract (Solidity)
- EduCertify.sol handles all on-chain logic
- Issues, verifies and revokes certificates
- Collects 0.001 ETH verification fee

### Layer 3 — Application (Python Web3.py)
- issue_certificate.py hashes PDF and registers on-chain
- verify_certificate.py checks certificate validity
- Connects to Sepolia via Infura RPC

### Layer 4 — User (MetaMask)
- Signs all transactions
- Holds Sepolia test ETH
- Connects wallet to Remix for deployment

## How The Layers Connect
User → Python Script → Smart Contract → Blockchain
```
