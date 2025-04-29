using MediatR;

namespace FinalLab.Application.Commands
{
    public class UpdateReactionCommand : IRequest
    {
        public long UserId { get; }
        public long ArticleId { get; }
        public int ReactionType { get; }

        public UpdateReactionCommand(long userId, long articleId, int reactionType)
        {
            UserId = userId;
            ArticleId = articleId;
            ReactionType = reactionType;
        }
    }
}

using MediatR;
