using MediatR;

namespace Main.Commands
{
    public class DeleteArticleCommand : IRequest
    {
        public int ArticleId { get; }

        public DeleteArticleCommand(int articleId)
        {
            ArticleId = articleId;
        }
    }
}
