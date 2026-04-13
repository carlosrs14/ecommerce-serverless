namespace Ecommerce.Shared.Models.Products;

public class UpdateProductRequest
{
    public string? Name { get; set; }
    public string? Brand { get; set; }
    public string? Description { get; set; }
    public string? Category { get; set; }
}
