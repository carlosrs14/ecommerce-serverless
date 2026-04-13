using System.Text.Json;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Ecommerce.Shared;
using Ecommerce.Shared.Models.Products;
using Ecommerce.Shared.Repositories;
using Microsoft.Extensions.DependencyInjection;

[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace Ecommerce.CreateProduct;

public class Function
{
    private readonly ServiceProvider _serviceProvider;

    public Function()
    {
        _serviceProvider = Startup.ConfigureServices();
    }

    public async Task<APIGatewayProxyResponse> FunctionHandler(APIGatewayProxyRequest request, ILambdaContext context)
    {
        using var scope = _serviceProvider.CreateScope();
        var _repository = scope.ServiceProvider.GetRequiredService<ProductsRepository>();
        try
        {
            var createRequest = JsonSerializer.Deserialize<CreateProductRequest>(request.Body, new JsonSerializerOptions
            {
                PropertyNameCaseInsensitive = true
            });

            if (createRequest == null)
            {
                return new APIGatewayProxyResponse { StatusCode = 400, Body = "Invalid request body" };
            }

            var productId = Guid.NewGuid().ToString();
            var product = new Product
            {
                PK = $"PRODUCT#{productId}",
                SK = $"PRODUCT#{productId}",
                Name = createRequest.Name,
                Brand = createRequest.Brand,
                Description = createRequest.Description,
                Category = createRequest.Category
            };

            await _repository.SaveProductAsync(product);

            return new APIGatewayProxyResponse
            {
                StatusCode = 201,
                Body = JsonSerializer.Serialize(product),
                Headers = new Dictionary<string, string> { { "Content-Type", "application/json" } }
            };
        }
        catch (Exception ex)
        {
            context.Logger.LogLine($"Error creating product: {ex.Message}");
            return new APIGatewayProxyResponse { StatusCode = 500, Body = "Internal Server Error" };
        }
    }
}
