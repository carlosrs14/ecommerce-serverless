import json
import boto3
import os

table_name = os.getenv('TABLE_NAME', 'ecommerce')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        product_id = event['pathParameters']['id']
        
        # Query para obtener el producto y sus ofertas en una sola llamada
        # PK = PRODUCT#<id>
        response = table.query(
            KeyConditionExpression=boto3.dynamodb.conditions.Key('PK').eq(f'PRODUCT#{product_id}')
        )
        
        items = response.get('Items', [])
        
        if not items:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Producto no encontrado'})
            }
        
        product = {}
        offers = []
        
        for item in items:
            if item['SK'] == f'PRODUCT#{product_id}':
                product = item
            elif item['SK'].startswith('OFFER#'):
                offers.append(item)
        
        # Combinar la información
        result = {
            **product,
            'offers': offers
        }
        
        return {
            'statusCode': 200,
            'body': json.dumps(result, default=str),
            'headers': {'Content-Type': 'application/json'}
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
