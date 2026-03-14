"""
verify_certificate.py
Verifies whether a certificate PDF is registered and valid on-chain.

Usage:
    python verify_certificate.py certificate_to_check.pdf
"""

import hashlib
import json
import sys
from web3 import Web3

# ── Configuration (fill these in after deployment) ──────────────
INFURA_URL    = 'https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID'
CONTRACT_ADDR = '0xYOUR_DEPLOYED_CONTRACT_ADDRESS'
VERIFIER_ADDR = '0xYOUR_METAMASK_WALLET_ADDRESS'
PRIVATE_KEY   = 'YOUR_PRIVATE_KEY'  # Never share this!

# ── Connect ──────────────────────────────────────────────────────
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

with open('abi/EduCertify_abi.json') as f:
    abi = json.load(f)
contract = w3.eth.contract(address=CONTRACT_ADDR, abi=abi)

# ── Hash the PDF ─────────────────────────────────────────────────
def hash_pdf(filepath):
    with open(filepath, 'rb') as f:
        return '0x' + hashlib.sha256(f.read()).hexdigest()

cert_file = sys.argv[1]
cert_hash = hash_pdf(cert_file)
print(f'Verifying hash: {cert_hash}')

# ── Read fee and verify ──────────────────────────────────────────
fee = contract.functions.verificationFee().call()
print(f'Verification fee: {w3.from_wei(fee, "ether")} ETH')

nonce = w3.eth.get_transaction_count(VERIFIER_ADDR)
tx = contract.functions.verifyCertificate(cert_hash).build_transaction({
    'from':     VERIFIER_ADDR,
    'value':    fee,
    'nonce':    nonce,
    'gas':      80000,
    'gasPrice': w3.to_wei('20', 'gwei'),
})

signed_tx = w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
tx_hash   = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
w3.eth.wait_for_transaction_receipt(tx_hash)

result = contract.functions.verifyCertificate(cert_hash).call(
    {'from': VERIFIER_ADDR, 'value': fee}
)

if result:
    print('RESULT: VALID — Certificate is registered and has not been revoked.')
else:
    print('RESULT: INVALID — Certificate not found or has been revoked.')
```

4. Commit message:
```
Add verify_certificate.py script
```
5. Extended description:
```
Python script that hashes a certificate PDF and verifies 
it against the EduCertify smart contract on Sepolia.
Sends 0.001 ETH as the DeFi verification fee.
