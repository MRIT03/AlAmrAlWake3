using MediatR;
using System.Collections.Generic;
using Main.Queries.DTO;

namespace Main.Queries
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
