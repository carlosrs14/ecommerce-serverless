using System.Text.Json;
using Amazon.DynamoDBv2;
using Amazon.Lambda.APIGatewayEvents;
using Amazon.Lambda.Core;
using Ecommerce.Shared;
using Ecommerce.Shared.Models.Products;
using Ecommerce.Shared.Repositories;
using Microsoft.Extensions.DependencyInjection;

[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]

namespace Ecommerce.UpdateProduct;

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
            if (!request.PathParameters.TryGetValue("id", out var productId))
            {
                return new APIGatewayProxyResponse { StatusCode = 400, Body = "Product ID is missing in path" };
            }

            var updateRequest = JsonSerializer.Deserialize<UpdateProductRequest>(request.Body, new JsonSerializerOptions
            {
                PropertyNameCaseInsensitive = true
            });

            if (updateRequest == null)
            {
                return new APIGatewayProxyResponse { StatusCode = 400, Body = "Invalid request body" };
            }

            var product = await _repository.GetProductAsync(productId);
            if (product == null)
            {
                return new APIGatewayProxyResponse { StatusCode = 404, Body = $"Product with ID {productId} not found" };
            }

            if (updateRequest.Name != null) product.Name = updateRequest.Name;
            if (updateRequest.Brand != null) product.Brand = updateRequest.Brand;
            if (updateRequest.Description != null) product.Description = updateRequest.Description;
            if (updateRequest.Category != null) product.Category = updateRequest.Category;

            await _repository.UpdateProductAsync(product);

            return new APIGatewayProxyResponse
            {
                StatusCode = 200,
                Body = JsonSerializer.Serialize(product),
                Headers = new Dictionary<string, string> { { "Content-Type", "application/json" } }
            };
        }
        catch (Exception ex)
        {
            context.Logger.LogLine($"Error updating product: {ex.Message}");
            return new APIGatewayProxyResponse { StatusCode = 500, Body = "Internal Server Error" };
        }
    }
}
