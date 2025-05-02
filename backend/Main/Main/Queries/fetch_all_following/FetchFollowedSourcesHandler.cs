using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Collections.Generic;
using Main.Data.Contexts;
using Main.Queries.DTOs;
using Main.Queries;
using MediatR;
using Microsoft.EntityFrameworkCore;

namespace Main.Handlers
{
    public class FetchFollowedSourcesHandler
        : IRequestHandler<FetchFollowedSourcesQuery, List<NewsSourceDto>>
    {
        private readonly AppDbContext _context;

        public FetchFollowedSourcesHandler(AppDbContext context)
            => _context = context;

        public async Task<List<NewsSourceDto>> Handle(
            FetchFollowedSourcesQuery request,
            CancellationToken cancellationToken)
        {
            var followedSources = await _context.Follows
                .Where(f => f.UserId == request.UserId)
                .Select(f => new NewsSourceDto
                {
                    SourceName = f.Source.SourceName,
                    SRR = f.Source.SRR,
                    IsFollowing = true
                })
                .ToListAsync(cancellationToken);

            return followedSources;
        }
    }
}