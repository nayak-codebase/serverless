import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
  # TODO implement
  dynamodb = boto3.resource('dynamodb')
  tableRatings = dynamodb.Table('Ratings')
  fe = Key('rating').eq("Excellent")
  fe1 = Key('rating').eq("Poor")
  response = tableRatings.scan(FilterExpression=fe)
  response1 = tableRatings.scan(FilterExpression=fe1)
  return {
    'statusCode': 200,
    'ExcellentRatingCount':str(len(response['Items'])),
    'PoorRatingCount': str(len(response1['Items'])),
    'headers':{ 'Access-Control-Allow-Origin' : '*' }

  }
