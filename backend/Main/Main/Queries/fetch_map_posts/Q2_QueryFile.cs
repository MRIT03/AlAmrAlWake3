
using MediatR;

namespace FinalLab.Application.Queries
{
    public class FetchHeadlinesQuery : IRequest<List<CityArticlesDto>>
    {
        public FetchHeadlinesQuery() { }
    }
}
