import json
import boto3
import os

table_name = os.getenv('TABLE_NAME', 'ecommerce')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        product_id = event['pathParameters']['id']
        
        # TODO  now soft delete -> delete offers too
        table.delete_item(
            Key={'PK': f'PRODUCT#{product_id}', 'SK': f'PRODUCT#{product_id}'}
        )
        
        return {
            'statusCode': 204,
            'body': json.dumps({'message': 'Producto eliminado'})
        }
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
