using MediatR;
using System.Collections.Generic;

namespace FinalLab.Application.Queries
{
    public class FetchFeedPostsQuery : IRequest<List<PostInfoDto>>
    {
        public long UserId { get; }

        public FetchFeedPostsQuery(long userId)
        {
            UserId = userId;
        }
    }
}
