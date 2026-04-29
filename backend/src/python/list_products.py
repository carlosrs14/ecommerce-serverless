import json
import boto3
import os

table_name = os.getenv('TABLE_NAME', 'ecommerce')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        # Scan filtrado por patrón de PK/SK para productos base
        # Nota: En producción con muchos datos, se prefiere un GSI "Type"
        response = table.scan(
            FilterExpression="begins_with(PK, :p) AND PK = SK",
            ExpressionAttributeValues={":p": "PRODUCT#"}
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(response.get('Items', []), default=str),
            'headers': {'Content-Type': 'application/json'}
        }
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
