using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Collections.Generic;
using Main.Data.Contexts;
using Main.Queries.DTO;
using Main.Queries;
using MediatR;
using Microsoft.EntityFrameworkCore;

namespace Main.Handlers
{
    public class FetchSearchResultsQueryHandler
        : IRequestHandler<FetchSearchResultsQuery, List<PostInfoDto>>
    {
        private readonly AppDbContext _context;

        public FetchSearchResultsQueryHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task<List<PostInfoDto>> Handle(
            FetchSearchResultsQuery request,
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

            // 2) Get the list of source-IDs this user follows
            var followedSourceIds = await _context.Follows
                .Where(f => f.UserId == request.UserId)
                .Select(f => f.SourceId)
                .ToListAsync(cancellationToken);

            // 3) Single query: filter by follow + headline search,
            //    include Region/Source/Reactions, group/count in SQL
            var raw = await _context.Articles
                .Where(a =>
                    followedSourceIds.Contains(a.SourceId) &&
                    EF.Functions.Like(a.Headline, $"%{request.SearchString}%"))
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

                    // this user's reaction, if any
                    SelectedReaction = a.Reactions
                        .Where(r => r.UserId == request.UserId)
                        .Select(r => r.ReactionType)
                        .FirstOrDefault(),

                    // counts per reaction type
                    ReactionGroups = a.Reactions
                        .GroupBy(r => r.ReactionType)
                        .Select(g => new { Type = g.Key, Count = g.Count() })
                        .ToList(),

                    // flags
                    FlagCount   = a.Reactions.Count(r => r.IsFlagged),
                    UserFlagged = a.Reactions
                        .Any(r => r.UserId == request.UserId && r.IsFlagged)
                })
                .ToListAsync(cancellationToken);

            // 4) Assemble the DTOs
            //    Define your expected reaction‐type order here:
            var reactionTypes = new[] { "Like", "Love", "Haha", "Sad", "Angry" };

            var results = raw.Select(a =>
            {
                var counters = reactionTypes
                    .Select(rt => a.ReactionGroups
                        .FirstOrDefault(g => g.Type == rt)?.Count ?? 0
                    )
                    .ToList();

                // append flag counts
                counters.Add(a.FlagCount);
                counters.Add(a.UserFlagged ? 1 : 0);

                return new PostInfoDto
                {
                    ArticleId        = a.ArticleId,
                    Headline         = a.Headline,
                    Body             = a.Body,
                    City             = a.City,
                    SourceName       = a.SourceName,
                    SRR              = 0,                // TODO: map your SRR field
                    PTS              = a.PTS,
                    TimeCreated      = a.TimeCreated,
                    DateTime         = a.TimeCreated,     // or combine ReactionDate+Time
                    SelectedReaction = a.SelectedReaction,
                    Counters         = counters,
                    IsAdmin          = "Verified"
                };
            })
            .ToList();

            return results;
        }
    }
}
