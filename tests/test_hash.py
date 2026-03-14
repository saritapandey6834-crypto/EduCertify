import hashlib

def hash_bytes(data: bytes) -> str:
    return '0x' + hashlib.sha256(data).hexdigest()

assert hash_bytes(b'Clark University degree') == hash_bytes(b'Clark University degree')
print('Test 1 passed: identical content produces identical hash')

hash_a = hash_bytes(b'Clark University degree')
hash_b = hash_bytes(b'Clark University Degree')
assert hash_a != hash_b
print('Test 2 passed: changed content produces different hash')

assert len(hash_bytes(b'test')) == 66
print('Test 3 passed: hash length is correct')

print('All tests passed!')
