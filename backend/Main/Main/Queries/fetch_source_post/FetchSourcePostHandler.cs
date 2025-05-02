using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Collections.Generic;
using Main.Data.Contexts;
using Main.Queries;
using Main.Queries.DTO;
using MediatR;
using Microsoft.EntityFrameworkCore;

namespace Main.Handlers
{
    public class FetchNewsOutletPostsQueryHandler
        : IRequestHandler<FetchNewsOutletPostsQuery, List<PostInfoDto>>
    {
        private readonly AppDbContext _context;
        public FetchNewsOutletPostsQueryHandler(AppDbContext context)
            => _context = context;

        public async Task<List<PostInfoDto>> Handle(
            FetchNewsOutletPostsQuery request,
            CancellationToken cancellationToken)
        {
            
            // // 1) Get user role once
            // var userRole = await _context.Users
            //     .Where(u => u.UserId == request.UserId)
            //     .Select(u => u.UserRole)
            //     .FirstOrDefaultAsync(cancellationToken);

            // bool isAdmin = string.Equals(
            //     userRole,
            //     "Admin",
            //     StringComparison.OrdinalIgnoreCase
            // );

            var raw = await _context.Articles
                .Where(a => a.SourceId == request.SourceId)
                .OrderByDescending(a => a.TimeCreated)
                .Select(a => new
                {
                    a.ArticleId,
                    a.Headline,
                    a.Body,
                    City        = a.Region.RegionName,
                    SourceName  = a.Source.SourceName,
                    PTS         = a.PTS,
                    TimeCreated = a.TimeCreated,

                    // this user’s own reaction (if any)
                    SelectedReaction = a.Reactions
                        .Where(r => r.UserId == request.UserId)
                        .Select(r => r.ReactionType)
                        .FirstOrDefault(),

                    // counts grouped by reaction type
                    ReactionGroups = a.Reactions
                        .GroupBy(r => r.ReactionType)
                        .Select(g => new { Type = g.Key, Count = g.Count() })
                        .ToList(),

                    // flag totals
                    FlagCount   = a.Reactions.Count(r => r.IsFlagged),
                    UserFlagged = a.Reactions
                        .Any(r => r.UserId == request.UserId && r.IsFlagged)
                })
                .ToListAsync(cancellationToken);

            // 3) Define your canonical reaction‐type order
            var reactionTypes = new[] { "Like", "Love", "Haha", "Sad", "Angry" };

            // 4) Shape into DTOs
            var posts = raw.Select(p =>
            {
                var counters = reactionTypes
                    .Select(rt => p.ReactionGroups
                        .FirstOrDefault(g => g.Type == rt)?.Count ?? 0
                    ).ToList();

                // append flags & user-flagged
                counters.Add(p.FlagCount);
                counters.Add(p.UserFlagged ? 1 : 0);

                return new PostInfoDto
                {
                    ArticleId        = p.ArticleId,
                    Headline         = p.Headline,
                    Body             = p.Body,
                    City             = p.City,
                    SourceName       = p.SourceName,
                    SRR              = 0,                  // map if you have SRR
                    PTS              = p.PTS,
                    TimeCreated      = p.TimeCreated,
                    DateTime         = p.TimeCreated,       // or build from ReactionDate+Time
                    SelectedReaction = p.SelectedReaction,
                    Counters         = counters,
                    IsAdmin          = "Verified"
                };
            })
            .ToList();

            return posts;
        }
    }
}
