from app.routers.role import role_router
import random
import fastapi
from fastapi.testclient import TestClient
from faker import Faker

fake = Faker('es_ES')

client = TestClient(role_router)

def custom_name(length):
    generated_name = fake.name()
    return generated_name[:length]


def test_get_roles():

    try:
        response = client.get("/role")
        assert response.status_code == 200, f"❌ Prueba fallida: test_get_roles. Código de estado: {response.status_code}"

        roles = response.json()
        assert isinstance(roles, list), "❌ Prueba fallida: test_get_roles. La respuesta no es una lista."
        
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
    except Exception as e:
        assert False, f"❌ Prueba fallida: test_get_roles. {e}"


def test_get_by_id_role():

    try:
        number_id = 14
        response = client.get(f"/role/{number_id}")

        if response.status_code == 200:
            
            role = response.json()
            assert response.status_code == 200, f"❌ Prueba fallida: test_get_by_id. Código de estado: {response.status_code}"
            assert isinstance(role, dict), "❌ Prueba fallida: test_get_by_id. La respuesta no es un diccionario."

            required_keys = ["id", "name", "state", "created_at", "updated_at"]
            for key in required_keys:
                assert key in role, f"❌ Prueba fallida: test_get_by_id. Faltan campos en el rol: {key}."

            assert isinstance(role["id"], int), "❌ Prueba fallida: test_get_by_id. El campo 'id' debe ser un entero."
            assert isinstance(role["name"], str), "❌ Prueba fallida: test_get_by_id. El campo 'name' debe ser una cadena."
            assert isinstance(role["state"], bool), "❌ Prueba fallida: test_get_by_id. El campo 'state' debe ser un booleano."
            assert isinstance(role["created_at"], str), "❌ Prueba fallida: test_get_by_id. El campo 'created_at' debe ser una cadena."
            assert isinstance(role["updated_at"], str), "❌ Prueba fallida: test_get_by_id. El campo 'updated_at' debe ser una cadena."

        print(f"✅ Prueba pasada: test_get_by_id. sen encontro el rol con id {number_id}.")

    except Exception as e:
        assert False, f"❌ Prueba fallida: test_get_by_id. {e}"


def test_get_by_id_role_validation_error_id_not_found():

    try:
        response = client.get(f"/role/0")

    except fastapi.exceptions.HTTPException as exc:
        if exc.status_code == 404:
            assert exc.detail == "Role not found", "✅ Prueba pasada: test_get_by_id. Mensaje de error correcto."
            print("✅ Prueba pasada: test_get_by_id. Se recibió el mensaje de error esperado Role not found")


def test_search_role_by_name():
    
    try:
        response = client.get(f"/role/search/Administrador")
        role = response.json()
        assert response.status_code == 200, f"❌ Prueba fallida: test_search_role_by_name. Código de estado: {response.status_code}"
        assert isinstance(role, dict), "❌ Prueba fallida: test_search_role_by_name. La respuesta no es un diccionario."

        required_keys = ["id", "name", "state", "created_at", "updated_at"]
        for key in required_keys:
            assert key in role, f"❌ Prueba fallida: test_search_role_by_name. Faltan campos en el rol: {key}."
        
        assert isinstance(role["id"], int), "❌ Prueba fallida: test_get_by_id. El campo 'id' debe ser un entero."
        assert isinstance(role["name"], str), "❌ Prueba fallida: test_get_by_id. El campo 'name' debe ser una cadena."
        assert isinstance(role["state"], bool), "❌ Prueba fallida: test_get_by_id. El campo 'state' debe ser un booleano."
        assert isinstance(role["created_at"], str), "❌ Prueba fallida: test_get_by_id. El campo 'created_at' debe ser una cadena."
        assert isinstance(role["updated_at"], str), "❌ Prueba fallida: test_get_by_id. El campo 'updated_at' debe ser una cadena."

    except Exception as e:
        assert False, f"❌ Prueba fallida: test_search_role_by_name. {e}"


def test_search_role_by_name_validation_error_name_not_found():
        
        try:
            response = client.get(f"/role/search/{custom_name(random.randint(1, 2))}")
    
        except fastapi.exceptions.HTTPException as exc:
            if exc.status_code == 404:
                assert exc.detail == "Role not found", "✅ Prueba pasada: test_search_role_by_name. Mensaje de error correcto."
                print("✅ Prueba pasada: test_search_role_by_name. Se recibió el mensaje de error esperado Role not found")


def test_post_role():
    try:
        new_role = {
            "name": custom_name(random.randint(3, 50)),
            "state": random.choice([True, False])
        }

        response = client.post("/role", json=new_role)
        role = response.json()
        assert response.status_code == 201, f"❌ Prueba fallida: test_post_role. Código de estado: {response.status_code}"
        assert isinstance(response.json(), dict), "❌ Prueba fallida: test_post_role. La respuesta no es un diccionario."
        
        assert isinstance(role["id"], int), "❌ Prueba fallida: test_get_by_id. El campo 'id' debe ser un entero."
        assert isinstance(role["name"], str), "❌ Prueba fallida: test_get_by_id. El campo 'name' debe ser una cadena."
        assert isinstance(role["state"], bool), "❌ Prueba fallida: test_get_by_id. El campo 'state' debe ser un booleano."
        assert isinstance(role["created_at"], str), "❌ Prueba fallida: test_get_by_id. El campo 'created_at' debe ser una cadena."
        assert isinstance(role["updated_at"], str), "❌ Prueba fallida: test_get_by_id. El campo 'updated_at' debe ser una cadena."
        print(f"✅ Prueba pasada: test_post_role. Se creó el rol con id {role['id']}.")
    except Exception as e:
        assert False, f"❌ Prueba fallida: test_post_role. {e}"


def test_post_role_validation_error_name_required():

    new_role = {
        "name": custom_name(random.randint(1, 2)),
        "state": random.choice([True, False])
    }

    try:
        response = client.post("/role", json=new_role)

    except fastapi.exceptions.RequestValidationError as exc:
        assert exc.errors()[0]['msg'] == 'String should have at least 3 characters', f"❌ Prueba fallida: test_update_role_validate_error_name_required. Mensaje de error incorrecto: {exc.errors()[0]['msg']}"
        print(f"✅ Prueba pasada: test_update_role_validate_error_name_required. Mensaje de error correcto: {exc.errors()[0]['msg']}")

def test_post_role_validation_error_name_max_length():
        
        new_role = {
            "name": 'a' *51,
            "state": random.choice([True, False])
        }
    
        try:
            response = client.post("/role", json=new_role)
    
        except fastapi.exceptions.RequestValidationError as exc:
            assert exc.errors()[0]['msg'] == 'String should have at most 50 characters', f"❌ Prueba fallida: test_update_role_validate_error_name_max_length. Mensaje de error incorrecto: {exc.errors()[0]['msg']}"
            print(f"✅ Prueba pasada: test_update_role_validate_error_name_max_length. Mensaje de error correcto")

def test_post_role_validation_error_role_exists():
    
        new_role = {
            "name": "Administrador",
            "state": random.choice([True, False])
        }
    
        try:
            response = client.post("/role", json=new_role)
            
        except fastapi.exceptions.HTTPException as exc:
            if exc.status_code == 400:
                assert exc.status_code == 400, "✅ Prueba pasada: test_post_role. Se recibió el código 400."
                assert exc.detail == "Role already exists", "✅ Prueba pasada: el mensaje de error es 'Role already exists'."
                print("✅ Prueba pasada: test_post_role. Se recibió el mensaje de error esperado : Role already exists.")


def test_update_role():

    name = custom_name(random.randint(3, 50))
    state = random.choice([True, False])
    
    update_role = {}
    if random.choice([True, False]):
        update_role["name"] = name
    if random.choice([True, False]):
        update_role["state"] = state

    if not update_role:
        update_role["name"] = name

    response = client.patch("/role/14", json=update_role)


    assert response.status_code == 200, f"❌ Prueba fallida: test_update_role. Código de estado: {response.status_code}"
    
    role = response.json()
    assert isinstance(role, dict), "❌ Prueba fallida: test_update_role. La respuesta no es un diccionario."

    required_keys = ["id", "name", "state", "created_at", "updated_at"]
    for key in required_keys:
        assert key in role, f"❌ Prueba fallida: test_update_role. Faltan campos en el rol: {key}."

    assert isinstance(role["id"], int), "❌ Prueba fallida: test_update_role. El campo 'id' debe ser un entero."
    assert isinstance(role["name"], str), "❌ Prueba fallida: test_update_role. El campo 'name' debe ser una cadena."
    assert isinstance(role["state"], bool), "❌ Prueba fallida: test_update_role. El campo 'state' debe ser un booleano."
    assert isinstance(role["created_at"], str), "❌ Prueba fallida: test_update_role. El campo 'created_at' debe ser una cadena."
    assert isinstance(role["updated_at"], str), "❌ Prueba fallida: test_update_role. El campo 'updated_at' debe ser una cadena."

    if "name" in update_role:
        assert role["name"] == update_role["name"], "❌ Prueba fallida: test_update_role. El nombre del rol no coincide."
    if "state" in update_role:
        assert role["state"] == update_role["state"], "❌ Prueba fallida: test_update_role. El estado del rol no coincide."

    print(f"✅ Prueba pasada: test_update_role. Se actualizó el rol con id {role['id']}.")


def test_update_role_validate_eror_id_not_found():
    
    update_role = {
        "name": custom_name(random.randint(3, 50)),
        "state": random.choice([True, False])
    }

    try:
        response = client.patch("/role/0", json=update_role)

    except fastapi.exceptions.HTTPException as exc:
        if exc.status_code == 404:
            assert exc.detail == "Role not found", "✅ Prueba pasada: test_update_role. Mensaje de error correcto."
            print("✅ Prueba pasada: test_update_role. Se recibió el mensaje de error esperado Role not found")

def test_update_role_validate_error_min_length_name():
    
    new_role = {
        "name": custom_name(random.randint(1, 2)),
        "state": random.choice([True, False])
    }

    try:
        response = client.patch("/role/6", json=new_role)

    except fastapi.exceptions.RequestValidationError as exc:
        assert exc.errors()[0]['msg'] == 'String should have at least 3 characters', f"❌ Prueba fallida: test_update_role_validate_error_name_required. Mensaje de error incorrecto: {exc.errors()[0]['msg']}"
        print(f"✅ Prueba pasada: test_update_role_validate_error_name_required. Mensaje de error correcto: {exc.errors()[0]['msg']}")

def test_update_role_validate_error_name_max_length():
        
        new_role = {
            "name": 'a' *51,
            "state": random.choice([True, False])
        }
    
        try:
            response = client.patch("/role/6", json=new_role)
    
        except fastapi.exceptions.RequestValidationError as exc:
            assert exc.errors()[0]['msg'] == 'String should have at most 50 characters', f"❌ Prueba fallida: test_update_role_validate_error_name_max_length. Mensaje de error incorrecto: {exc.errors()[0]['msg']}"
            print(f"✅ Prueba pasada: test_update_role_validate_error_name_max_length. Mensaje de error correcto")

def test_update_role_validate_error_role_exists():
    
        new_role = {
            "name": "Administrador",
            "state": random.choice([True, False])
        }
    
        try:
            response = client.patch("/role/15", json=new_role)
            
        except fastapi.exceptions.HTTPException as exc:
            if exc.status_code == 400:
                assert exc.status_code == 400, "✅ Prueba pasada: test_update_role. Se recibió el código 400."
                assert exc.detail == "Role with this name already exists", "✅ Prueba pasada: el mensaje de error es 'Role with this name already exists'."
                print("✅ Prueba pasada: test_update_role. Se recibió el mensaje de error esperado : Role with this name already exists.")

def test_delete_role():
    try:
        role_id = 14
        # Usar f-string para interpolar el valor de role_id en la URL
        response = client.delete(f"/role/{role_id}")
        role = response.json()
        assert response.status_code == 200, f"❌ Prueba fallida: test_delete_role. Código de estado: {response.status_code}"
        assert role["message"] == f"Role deleted successfully of id {role_id}", "❌ Prueba fallida: test_delete_role. Mensaje de error incorrecto."
    except Exception as e:
        assert False, f"❌ Prueba fallida: test_delete_role. {e}"


def test_delete_role_validate_error_id_not_found():
        
        try:
            response = client.delete("/role/0")
        except fastapi.exceptions.HTTPException as exc:
            if exc.status_code == 404:
                assert exc.detail == "Role not found", "✅ Prueba pasada: test_delete_role. Mensaje de error correcto."
                print("✅ Prueba pasada: test_delete_role. Se recibió el mensaje de error esperado Role not found")

def test_delete_role_validate_error_internal_server_error():
            
            try:
                response = client.delete("/role/1")
            except fastapi.exceptions.HTTPException as exc:
                if exc.status_code == 500:
                    assert exc.detail == "Internal server error", "✅ Prueba pasada: test_delete_role. Mensaje de error correcto."
                    print("✅ Prueba pasada: test_delete_role. Se recibió el mensaje de error esperado Internal server error")



