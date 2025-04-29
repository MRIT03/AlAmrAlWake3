using FinalLab.Application.Commands;
using FinalLab.Infrastructure.Persistence;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Threading;
using System.Threading.Tasks;

namespace FinalLab.Application.Handlers
{
    public class UpdateFollowingStateCommandHandler : IRequestHandler<UpdateFollowingStateCommand>
    {
        private readonly AppDbContext _context;

        public UpdateFollowingStateCommandHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task<Unit> Handle(UpdateFollowingStateCommand request, CancellationToken cancellationToken)
        {
            var followEntry = await _context.FOLLOW
                .FirstOrDefaultAsync(f => f.UserId == request.UserId && f.SourceId == request.SourceId, cancellationToken);

            if (followEntry != null)
            {
                // Delete the follow entry if it exists
                _context.FOLLOW.Remove(followEntry);
            }
            else
            {
                // Add a new follow entry if it doesn't exist
                followEntry = new Follow
                {
                    UserId = request.UserId,
                    SourceId = request.SourceId
                };
                await _context.FOLLOW.AddAsync(followEntry, cancellationToken);
            }

            await _context.SaveChangesAsync(cancellationToken);
            return Unit.Value;
        }
    }
}
