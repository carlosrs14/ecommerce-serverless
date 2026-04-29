import json
import boto3
import os

table_name = os.getenv('TABLE_NAME', 'ecommerce')
index_name = os.getenv('INDEX_NAME', 'GSI1')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        seller_id = event['pathParameters']['id']
        
        # Query usando GSI1 para obtener todas las ofertas del vendedor
        # GSI1PK = SELLER#<id>
        response = table.query(
            IndexName=index_name,
            KeyConditionExpression=boto3.dynamodb.conditions.Key('GSI1PK').eq(f'SELLER#{seller_id}')
        )
        
        items = response.get('Items', [])
        
        return {
            'statusCode': 200,
            'body': json.dumps(items, default=str),
            'headers': {'Content-Type': 'application/json'}
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
