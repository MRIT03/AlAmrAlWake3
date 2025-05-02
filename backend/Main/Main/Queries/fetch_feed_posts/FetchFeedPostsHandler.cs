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
    public class FetchFeedPostsQueryHandler
    : IRequestHandler<FetchFeedPostsQuery, List<PostInfoDto>>
{
    private readonly AppDbContext _context;
    public FetchFeedPostsQueryHandler(AppDbContext context)
    {
        _context = context;
    }

    public async Task<List<PostInfoDto>> Handle(
        FetchFeedPostsQuery request,
        CancellationToken cancellationToken)
    {
        // // 1) load the requesting user's role (so we can set IsAdmin)
        // var userRole = await _context.Users
        //     .Where(u => u.UserId == request.UserId)
        //     .Select(u => u.UserRole)
        //     .FirstOrDefaultAsync(cancellationToken);

        // bool isAdmin = string.Equals(userRole, "Admin", StringComparison.OrdinalIgnoreCase);

        // // 2) load the list of source-ids this user follows
        var followedSourceIds = await _context.Follows
            .Where(f => f.UserId == request.UserId)
            .Select(f => f.SourceId)
            .ToListAsync(cancellationToken);

        // 3) one big query to pull articles + region + source + reactions
        var raw = await _context.Articles
            .Where(a => followedSourceIds.Contains(a.SourceId))
            .OrderByDescending(a => a.TimeCreated)
            .Include(a => a.Region)
            .Include(a => a.Source)
            .Include(a => a.Reactions)
            .Select(a => new
            {
                // article basics
                a.ArticleId,
                a.Headline,
                a.Body,
                City       = a.Region.RegionName,
                SourceName = a.Source.SourceName,
                a.PTS,
                a.TimeCreated,

                // reaction by *this* user, if any
                SelectedReaction = a.Reactions
                    .Where(r => r.UserId == request.UserId)
                    .Select(r => r.ReactionType)
                    .FirstOrDefault(),

                // group counts by reaction type
                ReactionGroups = a.Reactions
                    .GroupBy(r => r.ReactionType)
                    .Select(g => new { Type = g.Key, Count = g.Count() })
                    .ToList(),

                // flagged‐counts
                FlagCount   = a.Reactions.Count(r => r.IsFlagged),
                UserFlagged = a.Reactions.Any(r =>
                                  r.UserId == request.UserId && r.IsFlagged)
            })
            .ToListAsync(cancellationToken);

        // 4) now shape into your DTOs
        var result = raw
            .Select(a =>
            {
                // build a List<int> of counts in a fixed order:
                // e.g. your app might recognize these as your 5 “standard” types
                var reactionTypes = new[] { "Like", "Love", "Haha", "Sad", "Angry" };

                var counters = reactionTypes
                    .Select(rt =>
                        a.ReactionGroups
                         .FirstOrDefault(g => g.Type == rt)?.Count ?? 0)
                    .ToList();

                // then append the flag‐counts
                counters.Add(a.FlagCount);
                counters.Add(a.UserFlagged ? 1 : 0);

                return new PostInfoDto
                {
                    ArticleId        = a.ArticleId,
                    Headline         = a.Headline,
                    Body             = a.Body,
                    City             = a.City,
                    SourceName       = a.SourceName,
                    PTS              = a.PTS,
                    TimeCreated      = a.TimeCreated,
                    DateTime         = a.TimeCreated,                // or combine ReactionDate + ReactionTime
                    IsAdmin          = "Verified",
                    SelectedReaction = a.SelectedReaction,
                    Counters         = counters
                };
            })
            .ToList();

        return result;
    }
}
}
