using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Main.Queries;
using Main.Data.Contexts;
using Main.Queries;
using Main.Queries.DTO;
using MediatR;
using Microsoft.EntityFrameworkCore;

namespace Main.Handlers
{
    public class FetchPostInfoQueryHandler
        : IRequestHandler<FetchPostInfoQuery, PostInfoDto>
    {
        private readonly AppDbContext _context;

        public FetchPostInfoQueryHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task<PostInfoDto> Handle(
            FetchPostInfoQuery request,
            CancellationToken cancellationToken)
        {
            // // 1) load the user's role once
            // var userRole = await _context.Users
            //     .Where(u => u.UserId == request.UserId)
            //     .Select(u => u.UserRole)
            //     .FirstOrDefaultAsync(cancellationToken);

            // bool isAdmin = string.Equals(
            //     userRole,
            //     "Admin",
            //     StringComparison.OrdinalIgnoreCase
            // );

            // 2) single query for the article + region + source + reactions
            var raw = await _context.Articles
                .Where(a => a.ArticleId == request.ArticleId)
                .Select(a => new
                {
                    a.ArticleId,
                    a.Headline,
                    a.Body,
                    City        = a.Region.RegionName,
                    SourceName  = a.Source.SourceName,
                    PTS         = a.PTS,
                    TimeCreated = a.TimeCreated,

                    // the reaction *this user* made (if any)
                    SelectedReaction = a.Reactions
                        .Where(r => r.UserId == request.UserId)
                        .Select(r => r.ReactionType)
                        .FirstOrDefault(),

                    // group‐and‐count every reaction type
                    ReactionGroups = a.Reactions
                        .GroupBy(r => r.ReactionType)
                        .Select(g => new { Type = g.Key, Count = g.Count() })
                        .ToList(),

                    // how many flags in total
                    FlagCount = a.Reactions.Count(r => r.IsFlagged),

                    // did *this* user flag it?
                    UserFlagged = a.Reactions.Any(r =>
                        r.UserId == request.UserId && r.IsFlagged)
                })
                .FirstOrDefaultAsync(cancellationToken);

            if (raw == null)
                return null; // or throw a NotFoundException, as you prefer

            // 3) build your fixed-order counters
            //    (replace these with your actual reaction-type strings)
            var reactionTypes = new[] { "Like", "Love", "Haha", "Sad", "Angry" };

            var counters = reactionTypes
                .Select(rt =>
                    raw.ReactionGroups.FirstOrDefault(g => g.Type == rt)?.Count
                    ?? 0
                )
                .ToList();

            // append the flag‐counts and user‐flagged
            counters.Add(raw.FlagCount);
            counters.Add(raw.UserFlagged ? 1 : 0);

            // 4) map into your DTO
            return new PostInfoDto
            {
                ArticleId        = raw.ArticleId,
                Headline         = raw.Headline,
                Body             = raw.Body,
                City             = raw.City,
                SourceName       = raw.SourceName,
                SRR              = 0,                      // TODO: map your SRR field here
                PTS              = raw.PTS,
                TimeCreated      = raw.TimeCreated,
                DateTime         = raw.TimeCreated,         // or combine ReactionDate+Time
                SelectedReaction = raw.SelectedReaction,
                Counters         = counters,
                IsAdmin          = "Verified"
            };
        }
    }
}
