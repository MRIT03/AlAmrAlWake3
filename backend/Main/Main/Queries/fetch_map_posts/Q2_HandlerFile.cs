using FinalLab.Application.DTOs;
using FinalLab.Application.Queries;
using FinalLab.Infrastructure.Persistence;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

namespace FinalLab.Application.Handlers
{
    public class FetchHeadlinesQueryHandler : IRequestHandler<FetchHeadlinesQuery, List<CityArticlesDto>>
    {
        private readonly AppDbContext _context;

        public FetchHeadlinesQueryHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task<List<CityArticlesDto>> Handle(FetchHeadlinesQuery request, CancellationToken cancellationToken)
        {
            var cityArticles = await _context.ARTICLE
                .Include(a => a.Region)
                .GroupBy(a => a.Region.RegionName)
                .Select(g => new CityArticlesDto
                {
                    City = g.Key,
                    Coordinates = new List<double> { g.First().Region.Latitude, g.First().Region.Longitude },
                    Articles = g.Select(a => new ArticleDto
                    {
                        ArticleId = a.ArticleId,
                        Headline = a.Headline
                    }).ToList()
                }).ToListAsync(cancellationToken);

            return cityArticles;
        }
    }
}
