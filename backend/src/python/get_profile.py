import json
import boto3
from dotenv import load_dotenv
import os

load_dotenv()
table_name = os.getenv('TABLE_NAME', 'ecommerce')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        user_id = event['queryStringParameters']['user_id']

        response = table.get_item(
            Key={
                'user_id': user_id
            }
        )
    
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Usuario no encontrado'})
            }

        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }