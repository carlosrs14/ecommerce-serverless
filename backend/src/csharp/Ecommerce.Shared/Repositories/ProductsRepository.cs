using Amazon.DynamoDBv2.DataModel;
using Ecommerce.Shared.Models.Products;

namespace Ecommerce.Shared.Repositories;

public class ProductsRepository(IDynamoDBContext context)
{
    private readonly IDynamoDBContext _context = context;

    public async Task SaveProductAsync(Product product)
    {
        await _context.SaveAsync(product);
    }

    public async Task<Product?> GetProductAsync(string id)
    {
        return await _context.LoadAsync<Product>($"PRODUCT#{id}", $"PRODUCT#{id}");
    }

    public async Task UpdateProductAsync(Product product)
    {
        await _context.SaveAsync(product);
    }
}
