using MediatR;
using System.Collections.Generic;
using Main.Queries.DTOs;

namespace Main.Queries
{
    public class FetchNewsSourcesQuery : IRequest<List<NewsSourceDto>>
    {
        public long UserId { get; }
        public string SearchString { get; }

        public FetchNewsSourcesQuery(long userId, string searchString)
        {
            UserId = userId;
            SearchString = searchString;
        }
    }
}
