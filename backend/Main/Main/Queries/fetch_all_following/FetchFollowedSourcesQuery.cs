using System.Collections.Generic;
using Main.Queries.DTOs;
using MediatR;

namespace Main.Queries
{
    public class FetchFollowedSourcesQuery : IRequest<List<NewsSourceDto>>
    {
        public int UserId { get; set; }

        public FetchFollowedSourcesQuery(int userId)
        {
            UserId = userId;
        }
    }
}
