using MediatR;
using System.Collections.Generic;
using Main.Queries.DTO;

namespace Main.Queries
{
    public class FetchSearchResultsQuery : IRequest<List<PostInfoDto>>
    {
        public long UserId { get; }
        public string SearchString { get; }

        public FetchSearchResultsQuery(long userId, string searchString)
        {
            UserId = userId;
            SearchString = searchString;
        }
    }
}
