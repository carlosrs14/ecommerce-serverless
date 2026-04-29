# AWS SAM Guide

Instrucciones para manejar el backend serverless.

## Requisitos
- AWS SAM CLI instalado.
- Docker (para pruebas locales).
- .NET 8 SDK, Python 3.12 y Go 1.25 instalados localmente para el `build`.

## Comandos Principales

### 1. Compilar el proyecto
Este comando detecta los diferentes runtimes (C#, Python, Go) y prepara los artefactos.
```bash
cd backend
sam build
```

### 2. Ejecutar API Localmente
Levanta un servidor local en el puerto 3000.
```bash
sam local start-api
```
- **Swagger UI:** [http://localhost:3000/docs](http://localhost:3000/docs)
- **OpenAPI Spec:** [http://localhost:3000/openapi.yaml](http://localhost:3000/openapi.yaml)

### 3. Despliegue en AWS
```bash
sam deploy --guided
```
Al finalizar, revisa la sección **Outputs** para obtener la URL de producción de Swagger.

## Notas de Desarrollo
- Si modificas el archivo `openapi.yaml` en `src/python/`, asegúrate de que el `CodeUri` en `template.yaml` lo incluya para que la Lambda de Swagger pueda leerlo.
- Para las Lambdas de C#, SAM compilará el `.csproj` automáticamente.
