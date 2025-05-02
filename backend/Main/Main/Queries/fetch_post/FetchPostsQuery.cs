using Main.Queries.DTO;
using MediatR;

namespace Main.Queries
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
