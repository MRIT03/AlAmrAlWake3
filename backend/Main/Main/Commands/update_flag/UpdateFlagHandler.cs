using Main.Commands;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Threading;
using System.Threading.Tasks;
using Main.Data.Contexts;
using Main.Entities;

namespace Main.Handlers
{
    public class UpdateFlagCommandHandler : IRequestHandler<UpdateFlagCommand>
    {
        private readonly AppDbContext _context;

        public UpdateFlagCommandHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task Handle(UpdateFlagCommand request, CancellationToken cancellationToken)
        {
            var reaction = await _context.Reactions
                .FirstOrDefaultAsync(r => r.UserId == request.UserId && r.ArticleId == request.ArticleId, cancellationToken);

            if (reaction != null)
            {
                // Update existing reaction
                reaction.IsFlagged = request.IsFlagged;
            }
            else
            {
                // Add new reaction with isFlagged set
                reaction = new Reaction
                {
                    UserId = request.UserId,
                    ArticleId = request.ArticleId,
                    IsFlagged = request.IsFlagged,
                    ReactionType = null // Set ReactionType to null
                };
                _context.Reactions.Add(reaction);
            }

            await _context.SaveChangesAsync(cancellationToken);

        }
    }
}
