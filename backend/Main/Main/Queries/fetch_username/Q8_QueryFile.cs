using MediatR;

namespace FinalLab.Application.Queries
{
    public class FetchUsernameQuery : IRequest<string>
    {
        public long UserId { get; }

        public FetchUsernameQuery(long userId)
        {
            UserId = userId;
        }
    }
}
