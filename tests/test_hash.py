import hashlib, unittest

class TestHashing(unittest.TestCase):

    def test_hash_length(self):
        digest = hashlib.sha256(b'Test content').digest()
        self.assertEqual(len(digest), 32)

    def test_hash_determinism(self):
        h1 = hashlib.sha256(b'Test content').digest()
        h2 = hashlib.sha256(b'Test content').digest()
        self.assertEqual(h1, h2)

    def test_hash_sensitivity(self):
        h1 = hashlib.sha256(b'Certificate A').digest()
        h2 = hashlib.sha256(b'Certificate B').digest()
        self.assertNotEqual(h1, h2)

if __name__ == '__main__':
    unittest.main()
