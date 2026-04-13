 # Actividad modelado orientado a consultas


## Pasos:
- 1. identificar los patrones de accesso
- 2. Diseñar llaves sobre cargadas con jerarqía



## Solución:

### 1. Patrones de acceso (preguntas)
#### Mi perfil
perfil del usuario
- nombre
- correo
- direcciones
- pagos
- foto

#### Pedidos recientes
Útlimos 10 pedidos del usuario
- estado
- fecha de creación
- dirección de envío

#### Detalle del pedido
Detalle de un pedido en específico
- id
- fecha
- dirección a donde va
- estado
- total
- items:
    - foto
    - nombre-producto
    - cantidad
    - precio-unitario
    - sub-total

### 2. Diseño de las llaves con sobre cargas (Single-Table Design)

| Entidad | PK | SK | GSI1PK | GSI1SK | Atributos |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Producto (Catálogo)** | `PRODUCT#<id>` | `PRODUCT#<id>` | - | - | Name, Brand, Description, EAN, Category |
| **Oferta (Vendedor)** | `PRODUCT#<id>` | `OFFER#<seller_id>` | `SELLER#<seller_id>` | `PRODUCT#<id>` | Price, Stock, Condition, Status |
| **Perfil Usuario** | `USER#<user_id>` | `PROFILE#<user_id>` | - | - | Name, Email, Photo |
| **Dirección Usuario** | `USER#<user_id>` | `ADDRESS#<addr_id>` | - | - | Street, City, ZipCode |
| **Pedido** | `USER#<user_id>` | `ORDER#<order_id>#<date>` | `ORDER#<order_id>` | `ORDER#<order_id>` | Status, Total, ShippingAddress |
| **Detalle Pedido** | `ORDER#<order_id>` | `ITEM#<product_id>` | - | - | Quantity, UnitPrice, SubTotal |

#### Notas:
- El **Catálogo** contiene la información técnica y global del producto.
- La **Oferta** vincula a un vendedor con un producto del catálogo, permitiendo diferentes precios y stocks para el mismo artículo.
- **GSI1** permite al vendedor consultar todas sus ofertas activas.



