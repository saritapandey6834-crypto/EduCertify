import hashlib, json
from web3 import Web3

RPC_URL       = 'https://sepolia.infura.io/v3/YOUR_PROJECT_ID'
CONTRACT_ADDR = '0x259Dd38221e099329A6f08Eb9e136B58E42D0A5e'
PRIVATE_KEY   = 'EMPLOYER_PRIVATE_KEY'

with open('abi/EduCertify_abi.json') as f:
    ABI = json.load(f)

w3       = Web3(Web3.HTTPProvider(RPC_URL))
account  = w3.eth.account.from_key(PRIVATE_KEY)
contract = w3.eth.contract(address=CONTRACT_ADDR, abi=ABI)

def hash_file(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            h.update(chunk)
    return h.digest()

cert_hash = hash_file('received_certificate.pdf')

tx = contract.functions.verifyCertificate(cert_hash).build_transaction({
    'from':  account.address,
    'nonce': w3.eth.get_transaction_count(account.address),
    'gas':   80_000,
    'gasPrice': w3.eth.gas_price,
    'value': w3.to_wei(0.001, 'ether'),
})
signed  = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
w3.eth.wait_for_transaction_receipt(tx_hash)

result = contract.functions.verifyCertificate(cert_hash).call(
    {'value': w3.to_wei(0.001, 'ether')}
)
print('VALID' if result else 'INVALID')

```
