import json
import boto3
import os

table_name = os.getenv('TABLE_NAME', 'ecommerce')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    try:
        product_id = event['pathParameters']['id']
        seller_id = event['pathParameters']['sellerId']
        body = json.loads(event.get('body', '{}'))
        
        price = body.get('price')
        stock = body.get('stock')
        
        if price is None and stock is None:
            return {'statusCode': 400, 'body': json.dumps({'message': 'Proporcione price o stock'})}

        update_expr = "SET "
        expr_vals = {}
        if price is not None:
            update_expr += "Price = :p, "
            expr_vals[':p'] = price
        if stock is not None:
            update_expr += "Stock = :s, "
            expr_vals[':s'] = stock
            
        update_expr = update_expr.rstrip(", ")

        response = table.update_item(
            Key={'PK': f'PRODUCT#{product_id}', 'SK': f'OFFER#{seller_id}'},
            UpdateExpression=update_expr,
            ExpressionAttributeValues=expr_vals,
            ReturnValues="ALL_NEW"
        )
        return {
            'statusCode': 200,
            'body': json.dumps(response.get('Attributes'), default=str),
            'headers': {'Content-Type': 'application/json'}
        }
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}
