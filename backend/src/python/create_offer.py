import json
import boto3
import os
from datetime import datetime

table_name = os.getenv('TABLE_NAME', 'ecommerce')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        product_id = event['pathParameters']['id']
        body = json.loads(event.get('body', '{}'))
        
        seller_id = body.get('sellerId')
        price = body.get('price')
        stock = body.get('stock')
        
        if not all([seller_id, price, stock]):
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Faltan campos obligatorios: sellerId, price, stock'})
            }
            
        # Verificar si el producto existe antes de crear la oferta
        product_check = table.get_item(
            Key={'PK': f'PRODUCT#{product_id}', 'SK': f'PRODUCT#{product_id}'}
        )
        
        if 'Item' not in product_check:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'El producto base no existe'})
            }

        offer_item = {
            'PK': f'PRODUCT#{product_id}',
            'SK': f'OFFER#{seller_id}',
            'GSI1PK': f'SELLER#{seller_id}',
            'GSI1SK': f'PRODUCT#{product_id}',
            'Price': price,
            'Stock': stock,
            'SellerId': seller_id,
            'ProductId': product_id,
            'CreatedAt': datetime.utcnow().isoformat()
        }
        
        table.put_item(Item=offer_item)
        
        return {
            'statusCode': 201,
            'body': json.dumps(offer_item, default=str),
            'headers': {'Content-Type': 'application/json'}
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
