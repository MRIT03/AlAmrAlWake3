using MediatR;

namespace Main.Commands
{
    public class UpdatePTSCommand : IRequest
    {
        public int ArticleId { get; set; }

        public UpdatePTSCommand(int articleId)
        {
            ArticleId = articleId;
        }
    }
}
