"""
issue_certificate.py
Hashes a certificate PDF and registers it on the EduCertify smart contract.

Usage:
    python issue_certificate.py certificate.pdf
"""

import hashlib
import json
import sys
from web3 import Web3

# ── Configuration (fill these in after deployment) ──────────────
INFURA_URL    = 'https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID'
CONTRACT_ADDR = '0xYOUR_DEPLOYED_CONTRACT_ADDRESS'
ISSUER_ADDR   = '0xYOUR_METAMASK_WALLET_ADDRESS'
PRIVATE_KEY   = 'YOUR_PRIVATE_KEY'  # Never share this!

# ── Connect to Sepolia ───────────────────────────────────────────
w3 = Web3(Web3.HTTPProvider(INFURA_URL))
print(f'Connected to Sepolia: {w3.is_connected()}')

# ── Load contract ABI ────────────────────────────────────────────
with open('abi/EduCertify_abi.json') as f:
    abi = json.load(f)
contract = w3.eth.contract(address=CONTRACT_ADDR, abi=abi)

# ── Hash the certificate PDF ─────────────────────────────────────
def hash_pdf(filepath):
    with open(filepath, 'rb') as f:
        file_bytes = f.read()
    return '0x' + hashlib.sha256(file_bytes).hexdigest()

# ── Main ─────────────────────────────────────────────────────────
cert_file = sys.argv[1]
cert_hash = hash_pdf(cert_file)
print(f'Certificate hash: {cert_hash}')

nonce = w3.eth.get_transaction_count(ISSUER_ADDR)
tx = contract.functions.issueCertificate(cert_hash).build_transaction({
    'from':     ISSUER_ADDR,
    'nonce':    nonce,
    'gas':      100000,
    'gasPrice': w3.to_wei('20', 'gwei'),
})

signed_tx = w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
tx_hash   = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
print(f'Transaction sent: {tx_hash.hex()}')

receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f'Confirmed in block: {receipt.blockNumber}')
print('Certificate successfully issued on-chain!')
```
