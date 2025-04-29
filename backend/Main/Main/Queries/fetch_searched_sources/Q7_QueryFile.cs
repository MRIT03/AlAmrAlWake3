using MediatR;
using System.Collections.Generic;

namespace FinalLab.Application.Queries
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
