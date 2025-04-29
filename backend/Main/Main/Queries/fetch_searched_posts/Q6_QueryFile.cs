using MediatR;
using System.Collections.Generic;

namespace FinalLab.Application.Queries
{
    public class FetchSearchResultsQuery : IRequest<List<PostInfoDTO>>
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
