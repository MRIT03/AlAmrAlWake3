using MediatR;

namespace FinalLab.Application.Commands
{
    public class LabelPostCommand : IRequest
    {
        public int ArticleId { get; }
        public string Label { get; }

        public LabelPostCommand(int articleId, string label)
        {
            ArticleId = articleId;
            Label = label;
        }
    }
}
