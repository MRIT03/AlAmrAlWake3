using MediatR;

namespace FinalLab.Application.Commands
{
    public class UpdateFlagCommand : IRequest
    {
        public int UserId { get; }
        public int ArticleId { get; }
        public bool IsFlagged { get; }

        public UpdateFlagCommand(int userId, int articleId, bool isFlagged)
        {
            UserId = userId;
            ArticleId = articleId;
            IsFlagged = isFlagged;
        }
    }
}
