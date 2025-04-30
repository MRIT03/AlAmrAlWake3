
using Main.Queries.DTOs;
using Main.Queries.DTO;
using MediatR;

namespace Main.Queries
{
 public class FetchHeadlinesQuery : IRequest<List<CityArticlesDto>>
 {
   public FetchHeadlinesQuery()
   {
   }
 }
}
