from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
import pytest
from src.Main import app
from src.Context.Repository.main import Engine, Session
from src.Context.Repository.Policie.policieRepository import policieRepository
from src.App.Policies.addPolicie import addPolicie

from uuid import UUID


mock_session = MagicMock()


client = TestClient(app)


@pytest.fixture()
def mock_engine_instance():
    return Engine()
    


def test_get_allPolicies():
    mockResponse = [{
        "id": "45fff0de-f78c-4b16-b00c-d2598829a5e1",
        "rutTitular": "string",
        "fechaEmision": "2025-08-07T01:53:55.563000",
        "planSalud": "string",
        "prima": 0,
        "estado": "Emitida"
    },
    {
        "id": "7c47a9a1-d667-4699-9a14-d12f23de29f4",
        "rutTitular": "string",
        "fechaEmision": "2025-08-07T01:53:55.563000",
        "planSalud": "string",
        "prima": 0,
        "estado": "Emitida"
    }]
    with patch.object(policieRepository, "getManyPolicies", return_value=mockResponse) as mock_getManyPolicies:
        response = client.get("/policies")
        assert response.status_code == 200
        assert response.json() == mockResponse
        mock_getManyPolicies.assert_called()


def test_get_policy_by_id():
    policy_id = "7c47a9a1-d667-4699-9a14-d12f23de29f4"
    mockResponse = {
        "id": "7c47a9a1-d667-4699-9a14-d12f23de29f4",
        "rutTitular": "string",
        "fechaEmision": "2025-08-07T01:53:55.563000",
        "planSalud": "string",
        "prima": 0,
        "estado": "Emitida"
    }
    with patch.object(policieRepository, "getPolicieById", return_value=mockResponse) as mock_getPolicieById:
        response = client.get(f"/policies/{policy_id}")
        assert response.status_code == 200
        assert response.json() == mockResponse
        mock_getPolicieById.assert_called()
        mock_getPolicieById.assert_called_with(UUID(policy_id))

def test_create_policy_already_exist():
    new_policy = {
        "id": "7c47a9a1-d667-4699-9a14-d12f23de29f4",
        "rutTitular": "string",
        "fechaEmision": "2025-08-07T01:53:55.563000",
        "planSalud": "string",
        "prima": 0,
        "estado": "Emitida"
    }
    mockResponse = {
        "id": "7c47a9a1-d667-4699-9a14-d12f23de29f4",
        "rutTitular": "string",
        "fechaEmision": "2025-08-07T01:53:55.563000",
        "planSalud": "string",
        "prima": 0,
        "estado": "Emitida"
    }
    with patch.object(policieRepository, "getPolicieById", return_value=None) as mock_getPolicieById:
        with patch.object(policieRepository, "addPolicie", return_value=mockResponse) as mock_addPolicie:
            response = client.post("/policies", json=new_policy)
            assert response.status_code == 201
            assert response.json() == mockResponse
            mock_addPolicie.assert_called()

# def test_update_policy():
#     policy_id = 1
#     update_data = {"test": "updatedValue"}
#     mockResponse = {"id": policy_id, "test": "updatedValue"}
#     response = client.put(f"/policies/{policy_id}", json=update_data)
#     assert response.status_code == 200
#     assert response.json() == mockResponse

# def test_delete_policy():
#     policy_id = 1
#     response = client.delete(f"/policies/{policy_id}")
#     assert response.status_code == 204
