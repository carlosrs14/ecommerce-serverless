# E-commerce Single Table Design

## Access Patterns

| Query | Use Case | Implementation |
| :--- | :--- | :--- |
| Get profile by email | GET `/api/v1/profile?user_id=...` | Get PK=`USER#id`, SK=`PROFILE#id` |
| Get user's orders | GET `/api/v1/users/{email}/orders` | Query GSI1PK=`USER#email`, GSI1SK begins with `ORDER#` |
| Get product & offers | GET `/api/v1/products/{id}` | Query PK=`PRODUCT#id` (Recupera Producto + todas sus OFERTAS) |
| Create/Update product | POST/PUT `/api/v1/products` | Put PK=`PRODUCT#id`, SK=`PRODUCT#id` |
| Create offer | POST `/api/v1/products/{id}/offers` | Put PK=`PRODUCT#id`, SK=`OFFER#sellerId` |
| Get seller's offers | GET `/api/v1/sellers/{id}/offers` | Query GSI1PK=`SELLER#id`, GSI1SK begins with `PRODUCT#` |

## Key Schema

| Entity | PK | SK | GSI1PK | GSI1SK | Attributes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **User Profile** | `USER#id` | `PROFILE#id` | - | - | `{name, photo, addresses}` |
| **Order (User View)**| `USER#email` | `ORDER#id` | `USER#email` | `ORDER#id` | `{total, status, date}` |
| **Order (System View)**| `ORDER#id` | `HEAD` | - | - | `{userEmail, total, status}` |
| **Order Item** | `ORDER#id` | `ITEM#productId` | - | - | `{quantity, price, subtotal}` |
| **Product (Catalog)**| `PRODUCT#id` | `PRODUCT#id` | - | - | `{name, brand, description, category}` |
| **Offer (Seller)** | `PRODUCT#id` | `OFFER#sellerId` | `SELLER#id` | `PRODUCT#id` | `{price, stock, sellerId}` |

## Key Condition Examples

| Query | Key Condition |
| :--- | :--- |
| **Product Detail Page** | Query PK=`PRODUCT#id`. <br>*Retorna el item del catálogo y todos los vendedores que lo ofrecen.* |
| **My Inventory (Seller)**| Query Index=`GSI1`, GSI1PK=`SELLER#id`, GSI1SK begins with `PRODUCT#`. |
| **User Orders** | Query Index=`GSI1`, GSI1PK=`USER#email`, GSI1SK begins with `ORDER#`. |
| **Order Items** | Query PK=`ORDER#id`, SK begins with `ITEM#`. |
| **List All Products** | Scan Filter `PK == SK` AND `PK begins with PRODUCT#`. <br>*Nota: Para grandes volúmenes, usar un GSI de tipo.* |
