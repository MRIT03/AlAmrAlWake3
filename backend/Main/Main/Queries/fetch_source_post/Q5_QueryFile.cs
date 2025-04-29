using MediatR;
using System.Collections.Generic;

namespace FinalLab.Application.Queries
{
    public class FetchNewsOutletPostsQuery : IRequest<List<FeedPostDto>>
    {
        public long SourceId { get; }

        public FetchNewsOutletPostsQuery(long sourceId)
        {
            SourceId = sourceId;
        }
    }
}
