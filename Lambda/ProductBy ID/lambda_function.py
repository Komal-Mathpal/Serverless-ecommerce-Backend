import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Products')

def lambda_handler(event, context):
    product_id = event['queryStringParameters']['product_id']
    response = table.get_item(Key={'product_id': product_id})
    
    item = response.get('Item', {})
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(item)
    }
