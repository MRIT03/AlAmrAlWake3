using MediatR;

namespace FinalLab.Application.Commands
{
    public class UpdateFollowingStateCommand : IRequest
    {
        public long UserId { get; }
        public long SourceId { get; }

        public UpdateFollowingStateCommand(long userId, long sourceId)
        {
            UserId = userId;
            SourceId = sourceId;
        }
    }
}
