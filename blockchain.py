
import hashlib

def blockchain_integration(data):
    hash_data = hashlib.sha256(data.encode()).hexdigest()
    return f"[Blockchain] Hash: {hash_data}"
