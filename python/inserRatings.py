import json
import boto3
from datetime import datetime
#That's the lambda handler, you can not modify this method
# the parameters from JSON body can be accessed like rating = event['rating']
def lambda_handler(event, context):
    # Instanciating connection objects with DynamoDB using boto3 dependency
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')
    
    # Getting the table the table rating object
    appRating = dynamodb.Table('Ratings')
    
    # Getting the current datetime and transforming it to string in the format bellow
    eventDateTime = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    rating = event['rating']
    
    # Putting a try/catch to log to user when some error occurs
    try:
        
        appRating.put_item(
           Item={
                'eventDateTime': eventDateTime,
                'rating': rating
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Succesfully inserted rating!'),
            'headers':{ 'Access-Control-Allow-Origin' : '*' }

        }
    except:
        print('Closing lambda function')
        return {
                'statusCode': 400,
                'body': json.dumps('Error saving the rating')
        }
