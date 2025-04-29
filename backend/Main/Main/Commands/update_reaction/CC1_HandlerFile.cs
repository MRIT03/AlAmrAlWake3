using FinalLab.Application.Commands;
using FinalLab.Infrastructure.Persistence;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Threading;
using System.Threading.Tasks;

namespace FinalLab.Application.Handlers
{
    public class AddOrUpdateReactionCommandHandler : IRequestHandler<AddOrUpdateReactionCommand>
    {
        private readonly AppDbContext _context;

        public AddOrUpdateReactionCommandHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task<Unit> Handle(AddOrUpdateReactionCommand request, CancellationToken cancellationToken)
        {
            var reaction = await _context.REACTION
                .FirstOrDefaultAsync(r => r.UserId == request.UserId && r.ArticleId == request.ArticleId, cancellationToken);

            if (reaction != null)
            {
                // Update existing reaction
                reaction.ReactionType = request.ReactionType;
                reaction.isFlagged = request.IsFlagged;
            }
            else
            {
                // Add new reaction
                reaction = new Reaction
                {
                    UserId = request.UserId,
                    ArticleId = request.ArticleId,
                    ReactionType = request.ReactionType,
                    isFlagged = request.IsFlagged
                };
                _context.REACTION.Add(reaction);
            }

            await _context.SaveChangesAsync(cancellationToken);

            return Unit.Value;
        }
    }
}