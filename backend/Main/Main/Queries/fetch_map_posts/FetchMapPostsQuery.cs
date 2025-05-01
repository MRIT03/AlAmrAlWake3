using MediatR;
using System.Collections.Generic;
using Main.Queries.DTO;

namespace Main.Queries
{
    public class FetchMapPostsQuery : IRequest<List<CityArticlesDto>>
    {
        public int UserId { get; set; }
        public bool OnlyFollowedSources { get; set; }
        public int Days { get; set; }
    }
}