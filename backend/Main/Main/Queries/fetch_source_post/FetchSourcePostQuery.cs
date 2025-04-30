using Main.Queries.DTO;
using MediatR;

namespace Main.Queries
{
    public class FetchNewsOutletPostsQuery : IRequest<List<PostInfoDto>>
    {
        public long SourceId { get; }
        public long UserId   { get; }

        public FetchNewsOutletPostsQuery(long sourceId, long userId)
        {
            SourceId = sourceId;
            UserId   = userId;
        }
    }
}