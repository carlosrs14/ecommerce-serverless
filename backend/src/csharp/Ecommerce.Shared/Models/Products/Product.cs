using Amazon.DynamoDBv2.DataModel;

namespace Ecommerce.Shared.Models.Products;

[DynamoDBTable("Ecommerce")]
public sealed class Product
{
    [DynamoDBHashKey]
    public string PK { get; init; } = string.Empty;

    [DynamoDBRangeKey]
    public string SK { get; init; } = string.Empty;

    
}