import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Products')  # replace with your table name

def lambda_handler(event, context):
    response = table.scan()
    items = response['Items']
    
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(items)
    }
