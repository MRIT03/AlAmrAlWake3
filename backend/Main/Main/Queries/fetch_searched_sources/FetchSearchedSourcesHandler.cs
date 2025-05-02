using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Collections.Generic;
using Main.Data.Contexts;
using Main.Queries;
using Main.Queries.DTOs;
using MediatR;
using Microsoft.EntityFrameworkCore;

namespace Main.Handlers
{
    public class FetchNewsSourcesQueryHandler
        : IRequestHandler<FetchNewsSourcesQuery, List<NewsSourceDto>>
    {
        private readonly AppDbContext _context;
        public FetchNewsSourcesQueryHandler(AppDbContext context)
            => _context = context;
    
        public async Task<List<NewsSourceDto>> Handle(
            FetchNewsSourcesQuery request,
            CancellationToken cancellationToken)
        {
            var raw = await _context.Sources
                .Where(s =>
                    EF.Functions.Like(s.SourceName, $"%{request.SearchString}%"))
                .Select(s => new
                {
                    s.SourceName,
                    s.SRR,
                    IsFollowing = s.Followers
                        .Any(f => f.UserId == request.UserId)
                })
                .ToListAsync(cancellationToken);

            // map into your DTO
            return raw
                .Select(r => new NewsSourceDto
                {
                    SourceName  = r.SourceName,
                    SRR = r.SRR,
                    IsFollowing = r.IsFollowing
                })
                .ToList();
        }
    }
}