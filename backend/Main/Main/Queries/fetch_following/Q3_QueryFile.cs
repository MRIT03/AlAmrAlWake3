using MediatR;

namespace FinalLab.Application.Queries
{
    public class IsFollowingSourceQuery : IRequest<bool> 
    {
        public long UserId { get; }
        public long SourceId { get; }

        public IsFollowingSourceQuery(long userId, long sourceId)
        {
            UserId = userId;
            SourceId = sourceId;
        }
    }
}