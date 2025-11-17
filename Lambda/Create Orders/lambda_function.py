import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
orders_table = dynamodb.Table('Orders')

def lambda_handler(event, context):
    try:
        print("Received event:", event)

        if 'body' in event and event['body']:
            body = json.loads(event['body'])
        else:
            body = event

        email = body.get('email')
        product_id = body.get('product_id')
        quantity = body.get('quantity', 1)

        if not email or not product_id:
            raise ValueError("Missing required fields: email or product_id")

        order_id = str(uuid.uuid4())
        orders_table.put_item(Item={
            'order_id': order_id,
            'user_email': email,
            'product_id': product_id,
            'quantity': quantity,
            'timestamp': datetime.utcnow().isoformat()
        })

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Order placed successfully', 'order_id': order_id})
        }

    except Exception as e:
        print("Error occurred:", e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    
