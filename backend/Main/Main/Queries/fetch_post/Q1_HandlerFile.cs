using FinalLab.Application.DTOs;
using FinalLab.Application.Queries;
using FinalLab.Infrastructure.Persistence;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

namespace FinalLab.Application.Handlers
{
    public class FetchPostInfoQueryHandler : IRequestHandler<FetchPostInfoQuery, PostInfoDto>
    {
        private readonly AppDbContext _context;

        public FetchPostInfoQueryHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task<PostInfoDto> Handle(FetchPostInfoQuery request, CancellationToken cancellationToken)
        {
            var article = await _context.ARTICLE
                .Include(a => a.Region)
                .Include(a => a.Source)
                .FirstOrDefaultAsync(a => a.ArticleId == request.ArticleId, cancellationToken);

            var user = await _context.USER
                .FirstOrDefaultAsync(u => u.UserId == request.UserId, cancellationToken);

            var selectedReaction = await _context.REACTION
                .Where(r => r.UserId == request.UserId && r.ArticleId == request.ArticleId)
                .Select(r => r.ReactionType)
                .FirstOrDefaultAsync(cancellationToken);

            var counters = await _context.REACTION
                .Where(r => r.ArticleId == request.ArticleId)
                .GroupBy(r => r.ReactionType)
                .Select(g => new { ReactionType = g.Key, Count = g.Count() })
                .ToListAsync(cancellationToken);

	   
	    var allReactionTypes = Enumerable.Range(0, 5)
                .Select(rt => new { ReactionType = rt, Count = counters.FirstOrDefault(c => 	   	   	c.ReactionType == rt)?.Count ?? 0 })
                .ToList();

            
	    var flagCount = await _context.REACTION
                .Where(r => r.ArticleId == request.ArticleId && r.isFlagged)
                .CountAsync(cancellationToken);
           
	    var userFlagged = await _context.REACTION
                .AnyAsync(r => r.UserId == request.UserId && r.ArticleId == request.ArticleId && 		r.isFlagged, cancellationToken);


            var postInfo = new PostInfoDto
            {
                City = article.Region.RegionName,
                SelectedReaction = selectedReaction,
		Counters = allReactionTypes.Select(c => c.Count).ToList(),
                Headline = article.Headline,
                Body = article.Body,
                SourceName = article.Source.SourceName,
                SRR = article.Source.SRR,
                PTS = article.PTS,
                DateTime = article.PTS,
                IsAdmin = article.Source.Admin // Assuming 'Admin' is a field in the 'SOURCE' table
            };

            postInfo.Counters.Add(flagCount);
            postInfo.Counters.Add(userFlagged ? 1 : 0);

            return postInfo;
        }
    }
}
