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


