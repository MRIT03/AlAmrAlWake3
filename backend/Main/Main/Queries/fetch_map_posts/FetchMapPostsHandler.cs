using Main.Queries.DTOs;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Main.Data.Contexts;
using Main.Queries;
using Main.Queries.DTO;

namespace Main.Handlers
{
    public class FetchMapPostsHandler : IRequestHandler<FetchMapPostsQuery, List<CityArticlesDto>>
    {
        private readonly AppDbContext _context;

        public FetchMapPostsHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task<List<CityArticlesDto>> Handle(FetchMapPostsQuery request, CancellationToken cancellationToken)
        {
            var dateThreshold = DateTime.UtcNow.AddDays(-request.Days);

            var query = _context.Articles
                .Include(a => a.Region)
                .Where(a => a.TimeCreated >= dateThreshold);

            if (request.OnlyFollowedSources)
            {
                query = query.Where(a =>
                    _context.Follows.Any(f =>
                        f.UserId == request.UserId &&
                        f.SourceId == a.SourceId));
            }

            var grouped = await query
                .GroupBy(a => a.Region.RegionName)
                .Select(g => new CityArticlesDto
                {
                    City = g.Key,
                    Coordinates = new List<double>
                    {
                        g.First().Region.Latitude,
                        g.First().Region.Longitude
                    },
                    Articles = g.Select(a => new ArticleDto
                    {
                        ArticleId = a.ArticleId,
                        Headline = a.Headline
                    }).ToList()
                })
                .ToListAsync(cancellationToken);

            return grouped;
        }
    }
}
