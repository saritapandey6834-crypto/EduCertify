# EduCertify — Deployment Steps

## Requirements
- MetaMask browser extension
- Sepolia test ETH from sepoliafaucet.com
- Remix IDE at remix.ethereum.org

## Step 1 — Compile
1. Open remix.ethereum.org
2. Create new file EduCertify.sol
3. Paste contract code
4. Select compiler version 0.8.0
5. Click Compile

## Step 2 — Deploy
1. Click Deploy & Run tab
2. Set Environment to Remix VM - Sepolia fork
3. Click Deploy
4. Copy contract address

## Step 3 — Test
1. Call issueCertificate with a bytes32 hash
2. Call verifyCertificate with same hash and 0.001 ETH
3. Confirm true is returned

## Contract Address
0x — update after deployment
```
