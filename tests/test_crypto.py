from app import crypto_service

def test_crypto_status():
    response = crypto_service.get_crypto_status()

    assert response["status"] == "ok"
