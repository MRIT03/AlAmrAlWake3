using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;
using Main.Data.Contexts;
using Main.Entities;
using Main.Queries.DTO;
using Microsoft.EntityFrameworkCore;

public class ArticleSyncService
{
    private readonly HttpClient _httpClient;
    private readonly AppDbContext _db;

    public ArticleSyncService(HttpClient httpClient, AppDbContext db)
    {
        _httpClient = httpClient;
        _db = db;
    }

    /// <summary>
    /// Fetches all articles up to the given date and stores any new ones.
    /// </summary>
    public async Task SyncArticlesUpToAsync(DateTime date)
    {
        // Format date as a string matching your Django URL
        var dateStr = date.ToString("yyyy-MM-dd");
        var response = await _httpClient.GetAsync($"articles/up-to/{dateStr}/");
        response.EnsureSuccessStatusCode();

        var json = await response.Content.ReadAsStringAsync();
        var articles = JsonSerializer.Deserialize<List<ArticleDto>>(json, new JsonSerializerOptions
        {
            PropertyNameCaseInsensitive = true
        });

        foreach (var dto in articles)
        {
            // Option A: skip if it already exists
            if (await _db.Articles.AnyAsync(a => a.ArticleId == dto.ArticleId))
                continue;

            // Map DTO → EF entity
            var entity = new Article
            {
                ArticleId   = dto.ArticleId,
                Headline    = dto.Headline,
                Body        = dto.Body,
                TimeCreated = dto.TimeCreated,
                PTS         = dto.Pts,
                SourceId    = dto.SourceId
            };

            _db.Articles.Add(entity);
        }

        await _db.SaveChangesAsync();
    }
}