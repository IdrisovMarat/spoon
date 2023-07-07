from fastapi.testclient import TestClient
from fast_api.main import  app
from fast_api.settings import settings


def test_answer():
    client = TestClient(app)
    result = client.get(settings.main_url)
    assert result.status_code == 200
    assert result.json() == {'status': 'ok'}

