package main

import (
	"context"
	"encoding/json"
	"os"

	"github.com/aws/aws-lambda-go/events"
	"github.com/aws/aws-lambda-go/lambda"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/feature/dynamodb/attributevalue"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb"
	"github.com/aws/aws-sdk-go-v2/service/dynamodb/types"
	models "github.com/carlosrs14/ecommerce-serverless/functions/get-orders/models"
)

type Response struct {
	Orders []models.Order `json:"orders"`
}

func handler(ctx context.Context, request events.APIGatewayProxyRequest) (events.APIGatewayProxyResponse, error) {
	email := request.PathParameters["email"]
	if email == "" {
		return events.APIGatewayProxyResponse{
			StatusCode: 400,
			Body:       `{"error": "email is required"}`,
		}, nil
	}

	tableName := os.Getenv("TABLE_NAME")
	indexName := os.Getenv("INDEX_NAME")
	if tableName == "" {
		return events.APIGatewayProxyResponse{
			StatusCode: 500,
			Body:       `{"error": "TABLE_NAME not set"}`,
		}, nil
	}

	cfg, err := config.LoadDefaultConfig(ctx)
	if err != nil {
		return events.APIGatewayProxyResponse{
			StatusCode: 500,
			Body:       `{"error": "failed to load config"}`,
		}, err
	}

	client := dynamodb.NewFromConfig(cfg)

	keyCondExpr := "GSI1PK = :pk AND begins_with(GSI1SK, :prefix)"
	result, err := client.Query(ctx, &dynamodb.QueryInput{
		TableName:              &tableName,
		IndexName:              &indexName,
		KeyConditionExpression: &keyCondExpr,
		ExpressionAttributeValues: map[string]types.AttributeValue{
			":pk":     &types.AttributeValueMemberS{Value: "USER#" + email},
			":prefix": &types.AttributeValueMemberS{Value: "ORDER#"},
		},
	})
	if err != nil {
		return events.APIGatewayProxyResponse{
			StatusCode: 500,
			Body:       `{"error": "failed to query orders"}`,
		}, err
	}

	var orders []models.Order
	for _, item := range result.Items {
		var order models.Order
		if err := attributevalue.UnmarshalMap(item, &order); err != nil {
			return events.APIGatewayProxyResponse{
				StatusCode: 500,
				Body:       `{"error": "failed to unmarshal order"}`,
			}, err
		}
		orders = append(orders, order)
	}

	body, _ := json.Marshal(Response{Orders: orders})
	return events.APIGatewayProxyResponse{
		StatusCode: 200,
		Body:       string(body),
		Headers:    map[string]string{"Content-Type": "application/json"},
	}, nil
}

func main() {
	lambda.Start(handler)
}
