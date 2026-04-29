# Ecommerce System

Un ecommerce desarrollado con una arquitectura serverless en el backend y una aplicación moderna en el frontend.

## Tecnologías

### Backend (Serverless)
- **Runtime:** .NET 8 (C#), Python 3.12, Golang 1.25
- **Infraestructura:** AWS Lambda con [AWS SAM](https://aws.amazon.com/serverless/sam/)
- **Base de Datos:** Amazon DynamoDB (Single-table design)
- **Caché:** Amazon ElastiCache (Redis) para perfiles.
- **API:** Amazon API Gateway + Swagger/OpenAPI 3.0

### Frontend
- **Framework:** Angular 19+
- **Estilos:** Vanilla CSS / Tailwind CSS
- **Testing:** Vitest / Angular CLI

## Estructura del Proyecto

```text
├── backend/                # Código del servidor (AWS SAM)
│   ├── src/csharp/         # Lambdas en .NET (Crear/Actualizar Producto)
│   ├── src/python/         # Lambdas en Python (Ofertas, Perfil, Swagger, Listados)
│   ├── src/go/             # Lambdas en Go (Órdenes)
│   └── template.yaml       # Definición de recursos AWS CloudFormation
├── frontend/               # Aplicación Angular
├── docs/                   # Documentación y modelos de datos (Patrones de acceso)
└── petitions/              # Ejemplos de peticiones HTTP (.http)
```

## Características Actuales
- **Catálogo de Productos:** Gestión base de productos (C# y Python).
- **Marketplace (Ofertas):** Los vendedores pueden publicar ofertas (precio/stock) sobre productos existentes.
- **Perfiles:** Obtención de perfiles con estrategia de caché (Cache-aside) en Redis.
- **Órdenes:** Consulta de historial de órdenes por usuario.
- **Documentación Interactiva:** Swagger UI integrado para pruebas rápidas.

## Configuración Local

### Backend
1. Instalar [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html).
2. Compilar y ejecutar localmente:
   ```bash
   cd backend
   sam build
   sam local start-api
   ```
3. **Documentación:** Una vez iniciado, accede a `http://localhost:3000/docs` para ver y probar la API.

### Frontend
1. Instalar dependencias:
   ```bash
   cd frontend
   npm install
   ```
2. Ejecutar servidor de desarrollo:
   ```bash
   npm start
   ```
