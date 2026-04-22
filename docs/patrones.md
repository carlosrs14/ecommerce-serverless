# E-commerce Single Table Design

## Access Patterns

| Query | Use Case |
| :--- | :--- |
| Get profile by email | GET `/api/v1/profile?email=user@example.com` |
| Get user's orders | GET `/api/v1/users/{email}/orders` |
| Get order details | GET `/api/v1/orders/{orderId}` |
| Create product | POST `/api/v1/products` |
| Update product | PUT `/api/v1/products/{id}` |

## Key Schema

| PK | SK | GSI1PK | GSI1SK | Attributes |
| :--- | :--- | :--- | :--- | :--- |
| `USER#email` | `PROFILE` | - | - | {name, photo, addresses, paymentMethods} |
| `USER#email` | `ORDER#orderId` | `USER#email` | `ORDER#orderId` | {date, address, total, status} |
| `ORDER#orderId` | `HEAD` | - | - | {date, address, total, status, userEmail} |
| `ORDER#orderId` | `ITEM#productId` | - | - | {quantity, price, subtotal} |
| `PRODUCT#id` | `PRODUCT#id` | - | - | {name, price, description, stock} |

## Key Condition Examples

| Query | Key Condition |
| :--- | :--- |
| My profile | Get PK=`USER#email`, SK=`PROFILE` |
| My orders | Query GSI1PK=`USER#email`, GSI1SK between `ORDER#` and `ORDER#\uffff` |
| Order details | Get PK=`ORDER#orderId`, SK=`HEAD` |
| Order items | Query PK=`ORDER#orderId`, SK begins with `ITEM#` |
| Product | Get PK=`PRODUCT#id`, SK=`PRODUCT#id` |