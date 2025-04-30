using MediatR;

namespace Main.Commands
{
    public class UpdateFollowingStateCommand : IRequest
    {
        public int UserId { get; }
        public int SourceId { get; }

        public UpdateFollowingStateCommand(int userId, int sourceId)
        {
            UserId = userId;
            SourceId = sourceId;
        }
    }
}
