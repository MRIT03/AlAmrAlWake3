using MediatR;

namespace Main.Commands
{
    public class UpdateReactionCommand : IRequest
    {
        public int UserId { get; }
        public int ArticleId { get; }
        public string ReactionType { get; }
        public bool IsFlagged { get; }

        public UpdateReactionCommand(int userId, int articleId, string reactionType)
        {
            UserId = userId;
            ArticleId = articleId;
            ReactionType = reactionType;
        }
    }
}


