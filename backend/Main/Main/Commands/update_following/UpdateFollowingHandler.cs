using FinalLab.Application.Commands;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Threading;
using System.Threading.Tasks;
using Main.Commands;
using Main.Data.Contexts;
using Main.Entities;

namespace Main.Handlers
{
    public class UpdateFollowingStateCommandHandler : IRequestHandler<UpdateFollowingStateCommand>
    {
        private readonly AppDbContext _context;

        public UpdateFollowingStateCommandHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task Handle(UpdateFollowingStateCommand request, CancellationToken cancellationToken)
        {
            var followEntry = await _context.Follows
                .FirstOrDefaultAsync(f => f.UserId == request.UserId && f.SourceId == request.SourceId, cancellationToken);

            if (followEntry != null)
            {
                // Delete the follow entry if it exists
                _context.Follows.Remove(followEntry);
            }
            else
            {
                // Add a new follow entry if it doesn't exist
                followEntry = new Follow
                {
                    UserId = request.UserId,
                    SourceId = request.SourceId
                };
                await _context.Follows.AddAsync(followEntry, cancellationToken);
            }

            await _context.SaveChangesAsync(cancellationToken);
        }
    }
}
