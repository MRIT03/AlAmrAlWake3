using System;
using System.Threading;
using System.Threading.Tasks;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

public class ArticleSyncWorker : BackgroundService
{
    private readonly IServiceScopeFactory _scopeFactory;
    private readonly ILogger<ArticleSyncWorker> _logger;

    public ArticleSyncWorker(
        IServiceScopeFactory scopeFactory,
        ILogger<ArticleSyncWorker> logger)
    {
        _scopeFactory = scopeFactory;
        _logger = logger;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        _logger.LogInformation("ArticleSyncWorker started");

        while (!stoppingToken.IsCancellationRequested)
        {
            try
            {
                using var scope = _scopeFactory.CreateScope();
                // resolve your sync service (which itself can resolve AppDbContext)
                var syncService = scope.ServiceProvider.GetRequiredService<ArticleSyncService>();

                _logger.LogInformation("Syncing articles at {time}", DateTimeOffset.Now);
                await syncService.SyncArticlesUpToAsync(DateTime.UtcNow.Date);
                _logger.LogInformation("Sync complete at {time}", DateTimeOffset.Now);
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error during article sync");
            }

            await Task.Delay(TimeSpan.FromHours(1), stoppingToken);
        }

        _logger.LogInformation("ArticleSyncWorker stopping");
    }
}