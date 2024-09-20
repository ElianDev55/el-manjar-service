from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

async def custom_validation_error_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        error_detail = {
            "campo": error["loc"][-1] if error["loc"] else "desconocido",
            "tipo_error": error["type"],
            "mensaje": error["msg"]
        }
        
        if error["type"] == "missing":
            error_detail["mensaje"] = f"El campo '{error_detail['campo']}' es obligatorio y no fue proporcionado."
        
        errors.append(error_detail)

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "Error de validación en los datos de entrada",
            "detalles": errors
        }
    )