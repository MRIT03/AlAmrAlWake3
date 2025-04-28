using MediatR;

namespace FinalLab.Application.Queries
{
    public class FetchPostInfoQuery : IRequest<PostInfoDto>
    {
        public long ArticleId { get; }
        public long UserId { get; }

        public FetchPostInfoQuery(long articleId, long userId)
        {
            ArticleId = articleId;
            UserId = userId;
        }
    }
}
