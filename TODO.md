# TODO - E-commerce Backend (.NET & DynamoDB)

Este archivo contiene las tareas pendientes para completar el flujo de **Catálogo y Ofertas** estilo Mercado Libre.

## 1. Gestión de Ofertas (Vendedores)
- [ ] **Crear Lambda `CreateOffer`:** Implementar POST `/api/v1/products/{id}/offers` para que un vendedor publique un producto del catálogo.
- [ ] **Crear Lambda `UpdateOffer`:** Implementar PUT `/api/v1/products/{id}/offers/{sellerId}` para actualizar precio o stock.
- [ ] **Modelo de Datos de Oferta:** Implementar la clase `Offer` en `Ecommerce.Shared` con `PK = PRODUCT#<id>` y `SK = OFFER#<seller_id>`.
- [ ] **Configurar GSI1:** Asegurar que al guardar una oferta se incluyan `GSI1PK = SELLER#<id>` y `GSI1SK = PRODUCT#<id>` para búsquedas inversas.

## 2. Consultas y Vistas (Read Models)
- [ ] **Vista de Producto (Buyer View):** Crear Lambda `GetProduct` (GET `/api/v1/products/{id}`) que devuelva la información del catálogo **Y** la lista de ofertas de todos los vendedores en una sola consulta de DynamoDB (Query por PK).
- [ ] **Vista del Vendedor (Seller View):** Crear Lambda `GetSellerOffers` (GET `/api/v1/sellers/{id}/offers`) usando el `GSI1` para listar todo lo que vende un usuario específico.
- [ ] **Búsqueda por Categoría:** Implementar un GSI adicional o aprovechar los existentes para filtrar productos del catálogo por categoría.

## 3. Mejoras Técnicas e Infraestructura
- [ ] **Desacoplamiento de Tabla:** Modificar `ProductsRepository.cs` para obtener el nombre de la tabla de la variable de entorno `TABLE_NAME` en lugar de tenerlo fijo.
- [ ] **Validaciones de Integridad:** Validar que el `productId` exista en el catálogo antes de permitir crear una oferta para él.
- [ ] **Configuración de CORS:** Habilitar CORS en `template.yaml` para permitir peticiones desde el frontend (Angular).
- [ ] **Documentación API:** Actualizar `petitions/example.http` con ejemplos de ofertas y consultas GET.

## 4. Integración Frontend
- [ ] **Conexión Angular:** Actualizar los servicios del frontend en `/frontend/src/app/` para consumir los nuevos endpoints de productos y ofertas.
