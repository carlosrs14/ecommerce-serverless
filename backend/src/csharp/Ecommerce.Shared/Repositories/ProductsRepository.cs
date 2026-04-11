
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;

namespace Ecommerce.Shared.Repositories;

public class ProductsRepository
{
    private readonly AmazonDynamoDBClient _client = new();

    public async Task SaveProductAsync()
    {
        var item = new Dictionary<string, AttributeValue>
        {
            // TODO parse items
        };
        
        await _client.PutItemAsync(
            new PutItemRequest
            {
                TableName = "Ecommerce",
                Item = item
            }
        );
    }

}