from fastapi.testclient import TestClient
from app.routers.role import role_router


client = TestClient(role_router)


def test_get_roles():
    response = client.get("/role")
    assert response.status_code == 200, f"❌ Prueba fallida: test_get_roles. Código de estado: {response.status_code}"

    roles = response.json()
    assert isinstance(roles, list), "❌ Prueba fallida: test_get_roles. La respuesta no es una lista."
    
    assert len(roles) > 0, "❌ Prueba fallida: test_get_roles. No se encontraron roles."

    first_role = roles[0]
    required_keys = ["id", "name", "state", "created_at", "updated_at"]
    
    for key in required_keys:
        assert key in first_role, f"❌ Prueba fallida: test_get_roles. Faltan campos en el primer rol: {key}."

    assert isinstance(first_role["id"], int), "❌ Prueba fallida: test_get_roles. El campo 'id' debe ser un entero."
    assert isinstance(first_role["name"], str), "❌ Prueba fallida: test_get_roles. El campo 'name' debe ser una cadena."
    assert isinstance(first_role["state"], bool), "❌ Prueba fallida: test_get_roles. El campo 'state' debe ser un booleano."
    assert isinstance(first_role["created_at"], str), "❌ Prueba fallida: test_get_roles. El campo 'created_at' debe ser una cadena."
    assert isinstance(first_role["updated_at"], str), "❌ Prueba fallida: test_get_roles. El campo 'updated_at' debe ser una cadena."

    print(f"✅ Prueba pasada: test_get_roles. Se encontraron {len(roles)} roles.")

def test_get_by_id():

    response = client.get("/role/6")
    assert response.status_code == 200, f"❌ Prueba fallida: test_get_by_id. Código de estado: {response.status_code}"
    
    role = response.json()
    assert isinstance(role, dict), "❌ Prueba fallida: test_get_by_id. La respuesta no es un diccionario."

    required_keys = ["id", "name", "state", "created_at", "updated_at"]
    
    for key in required_keys:
        assert key in role, f"❌ Prueba fallida: test_get_by_id. Faltan campos en el rol: {key}."

    assert isinstance(role["id"], int), "❌ Prueba fallida: test_get_by_id. El campo 'id' debe ser un entero."
    assert isinstance(role["name"], str), "❌ Prueba fallida: test_get_by_id. El campo 'name' debe ser una cadena."
    assert isinstance(role["state"], bool), "❌ Prueba fallida: test_get_by_id. El campo 'state' debe ser un booleano."
    assert isinstance(role["created_at"], str), "❌ Prueba fallida: test_get_by_id. El campo 'created_at' debe ser una cadena."
    assert isinstance(role["updated_at"], str), "❌ Prueba fallida: test_get_by_id. El campo 'updated_at' debe ser una cadena."

    print("✅ Prueba pasada: test_get_by_id.")
