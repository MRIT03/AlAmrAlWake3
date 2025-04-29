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
    public class FetchNewsOutletPostsQueryHandler : IRequestHandler<FetchNewsOutletPostsQuery, List<PostInfoDTO>>
    {
        private readonly AppDbContext _context;

        public FetchNewsOutletPostsQueryHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task<List<PostInfoDTO>> Handle(FetchNewsOutletPostsQuery request, CancellationToken cancellationToken)
        {
            var posts = await _context.ARTICLE
                .Include(a => a.Region)
                .Include(a => a.Source)
                .Where(a => a.SourceId == request.SourceId)
                .OrderByDescending(a => a.TimeCreated)
                .Select(a => new PostInfoDTO
                {
                    City = a.Region.RegionName,
                    SelectedReaction = _context.REACTION
                        .Where(r => r.UserId == request.UserId && r.ArticleId == a.ArticleId)
                        .Select(r => r.ReactionType)
                        .FirstOrDefault(),

		    Counters = Enumerable.Range(0, 6)
                        .Select(rt => _context.REACTION
                        .Where(r => r.ArticleId == a.ArticleId && r.ReactionType == rt)
                        .Count())
                        .ToList(),

                    Headline = a.Headline,
                    Body = a.Body,
                    SourceName = a.Source.SourceName,
                    SRR = a.Source.SRR,
                    PTS = a.PTS,
                    TimeCreated = a.TimeCreated,
                    IsAdmin = a.Source.Admin 
                })
                .ToListAsync(cancellationToken);

	    foreach (var post in posts)
            {
                var flagCount = await _context.REACTION
                    .Where(r => r.ArticleId == post.ArticleId && r.isFlagged)
                    .CountAsync(cancellationToken);

                var userFlagged = await _context.REACTION
                    .AnyAsync(r => r.UserId == request.UserId && r.ArticleId == post.ArticleId && r.isFlagged, cancellationToken);

                post.Counters.Add(flagCount);
                post.Counters.Add(userFlagged ? 1 : 0);
            }


            return posts;
        }
    }
}
