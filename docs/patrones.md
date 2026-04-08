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

### 2. Diseño de las llaves con sobre cargas

#### Diseño de tabla (Single Table Design)

| PK | SK | Data |
| :--- | :--- | :--- |
| USER#email | PROFILE | {Nombre, Foto, Direcciones, MetodosPago} |
| USER#email | ORDER#orderId | {Fecha, Direccion, Total, Estado} |
| USER#email | PAYMENT#orderId | {Monto, Metodo, Fecha, Estatus} |
| ORDER#orderId | HEAD | {Fecha, Direccion, Total, Estado} |
| ORDER#orderId | ITEM#productId | {Cantidad, Precio, Subtotal} |

#### Patrones de consulta

| Query | Key Condition |
| :--- | :--- |
| Mi perfil | Get PK=USER#email, SK=PROFILE |
| Mis pedidos (todos) | Query PK=USER#email, SK between ORDER# and ORDER#\uffff |
| Detalle del pedido | Get PK=ORDER#orderId, SK=HEAD |
| Items del pedido | Query PK=ORDER#orderId, SK begins with ITEM# |
| Payment del pedido | Get PK=USER#email, SK=PAYMENT#orderId |

