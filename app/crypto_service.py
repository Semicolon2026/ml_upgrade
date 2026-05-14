from cryptography.fernet import Fernet
import cryptography

def get_crypto_status():
    key = Fernet.generate_key()

    return {
        "status": "ok",
        "library": "cryptography",
        "version": cryptography.__version__,
        "key_generated": True
    }
