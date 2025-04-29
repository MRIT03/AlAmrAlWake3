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
    public class FetchNewsSourcesQueryHandler : IRequestHandler<FetchNewsSourcesQuery, List<NewsSourceDto>>
    {
        private readonly AppDbContext _context;

        public FetchNewsSourcesQueryHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task<List<NewsSourceDto>> Handle(FetchNewsSourcesQuery request, CancellationToken cancellationToken)
        {
            var followedSources = await _context.FOLLOW
                .Where(f => f.UserId == request.UserId)
                .Select(f => f.SourceId)
                .ToListAsync(cancellationToken);

            var sources = await _context.SOURCE
                .Where(s => EF.Functions.Like(s.SourceName, $"%{request.SearchString}%"))
                .Select(s => new NewsSourceDto
                {
                    SourceName = s.SourceName,
                    SRR = s.SRR,
                    IsFollowing = followedSources.Contains(s.SourceId)
                })
                .ToListAsync(cancellationToken);

            return sources;
        }
    }
}
