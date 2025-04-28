using FinalLab.Application.Queries;
using FinalLab.Infrastructure.Persistence;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Threading;
using System.Threading.Tasks;

namespace FinalLab.Application.Handlers
{
    public class FetchUsernameQueryHandler : IRequestHandler<FetchUsernameQuery, string>
    {
        private readonly AppDbContext _context;

        public FetchUsernameQueryHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task<string> Handle(FetchUsernameQuery request, CancellationToken cancellationToken)
        {
            var user = await _context.USER
                .Where(u => u.UserId == request.UserId)
                .Select(u => u.Username)
                .FirstOrDefaultAsync(cancellationToken);

            return user;
        }
    }
}
