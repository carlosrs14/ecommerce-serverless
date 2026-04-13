# Ecommerce System

Un ecommerce desarrollado con una arquitectura serverless en el backend y una aplicación moderna en el frontend.

## Tecnologías

### Backend (Serverless)
- **Runtime:** .NET 8 (C#), Python 3.13, Golang
- **Infraestructura:** AWS Lambda con [AWS SAM](https://aws.amazon.com/serverless/sam/)
- **Base de Datos:** Amazon DynamoDB (Single-table design)
- **API:** Amazon API Gateway

### Frontend
- **Framework:** Angular 21
- **Estilos:** Tailwind CSS
- **Testing:** Vitest

## Estructura del Proyecto

```text
├── backend/                # Código del servidor (AWS SAM)
│   ├── src/csharp/         # Lambdas en .NET
│   ├── src/python/         # Lambdas en Python
│   └── template.yaml       # Definición de recursos AWS CloudFormation
├── frontend/               # Aplicación Angular
├── docs/                   # Documentación y modelos de datos
└── petitions/              # Ejemplos de peticiones HTTP (.http)
```

## Características Actuales
- **Gestión de Productos:** Creación y actualización de productos en el catálogo central.
- **Perfiles:** Obtención de información de perfil de usuario.
- **Diseño de Datos:** Implementación de GSI en DynamoDB para consultas eficientes de productos y ofertas.

## Configuración Local

### Backend
1. Instalar [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html).
2. Compilar y desplegar localmente:
   ```bash
   cd backend
   sam build
   sam local start-api
   ```

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
