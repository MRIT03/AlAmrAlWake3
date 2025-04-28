using FinalLab.Application.Queries;
using FinalLab.Infrastructure.Persistence;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Threading;
using System.Threading.Tasks;

namespace FinalLab.Application.Handlers
{
    public class IsFollowingSourceHandler : IRequestHandler<IsFollowingSourceQuery, bool>
    {
        private readonly AppDbContext _context; // Assuming you have a DbContext

        public IsFollowingSourceHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task<bool> Handle(IsFollowingSourceQuery request, CancellationToken cancellationToken)
        {
            return await _context.FOLLOW
                .AnyAsync(f => f.UserId == request.UserId && f.SourceId == request.SourceId, cancellationToken);
        }
    }
}
