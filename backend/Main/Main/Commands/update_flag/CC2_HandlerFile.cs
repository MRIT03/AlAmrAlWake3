using FinalLab.Application.Commands;
using FinalLab.Infrastructure.Persistence;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Threading;
using System.Threading.Tasks;

namespace FinalLab.Application.Handlers
{
    public class UpdateFlagCommandHandler : IRequestHandler<UpdateFlagCommand>
    {
        private readonly AppDbContext _context;

        public UpdateFlagCommandHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task<Unit> Handle(UpdateFlagCommand request, CancellationToken cancellationToken)
        {
            var reaction = await _context.REACTION
                .FirstOrDefaultAsync(r => r.UserId == request.UserId && r.ArticleId == request.ArticleId, cancellationToken);

            if (reaction != null)
            {
                // Update existing reaction
                reaction.isFlagged = request.IsFlagged;
            }
            else
            {
                // Add new reaction with isFlagged set
                reaction = new Reaction
                {
                    UserId = request.UserId,
                    ArticleId = request.ArticleId,
                    isFlagged = request.IsFlagged,
                    ReactionType = null // Set ReactionType to null
                };
                _context.REACTION.Add(reaction);
            }

            await _context.SaveChangesAsync(cancellationToken);

            return Unit.Value;
        }
    }
}
