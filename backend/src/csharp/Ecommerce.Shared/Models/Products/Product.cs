using Amazon.DynamoDBv2.DataModel;

namespace Ecommerce.Shared.Models.Products;

[DynamoDBTable("ecommerce")]
public sealed class Product
{
    [DynamoDBHashKey]
    public string PK { get; set; } = string.Empty; // PRODUCT#<id>

    [DynamoDBRangeKey]
    public string SK { get; set; } = string.Empty; // PRODUCT#<id>

    public string Name { get; set; } = string.Empty;
    public string Brand { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public string? EAN { get; set; }
    public string Category { get; set; } = string.Empty;
}
