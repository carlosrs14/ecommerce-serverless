import json
import boto3
from dotenv import load_dotenv
import os
import redis  

load_dotenv()

table_name = os.getenv('TABLE_NAME', 'ecommerce')
cache_endpoint = os.getenv('CACHE_ENDPOINT') 

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

cache = redis.Redis(
    host=cache_endpoint,
    port=6379,
    decode_responses=True,
    ssl=True
)

def lambda_handler(event, context):
    try:
        user_id = event['queryStringParameters']['user_id']
        cache_key = f"profile:{user_id}"

        try:
            cached = cache.get(cache_key)
        except Exception:
            cached = None

        if cached:
            return {
                'statusCode': 200,
                'body': cached,
                'headers': {'X-Cache': 'HIT'}
            }

        response = table.get_item(
            Key={
                'PK': f'USER#{user_id}',
                'SK': f'PROFILE#{user_id}'
            }
        )
    
        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Usuario no encontrado'})
            }

        item = response['Item']

        try:
            cache.setex(cache_key, 60, json.dumps(item))
        except Exception:
            pass

        return {
            'statusCode': 200,
            'body': json.dumps(item),
            'headers': {'X-Cache': 'MISS'}
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }