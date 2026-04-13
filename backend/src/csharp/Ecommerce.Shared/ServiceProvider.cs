using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.DataModel;
using Ecommerce.Shared.Repositories;

namespace Ecommerce.Shared;

public class Startup
{
    public static ServiceProvider ConfigureServices()
    {
        var services = new ServiceCollection();

        services.AddAWSService<IAmazonDynamoDB>();
        services.AddScoped<IDynamoDBContext, DynamoDBContext>();

        services.AddScoped<ProductsRepository>();

        return services.BuildServiceProvider();
    }
}