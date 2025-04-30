using FinalLab.Application.Commands;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Threading;
using System.Threading.Tasks;
using Main.Commands;
using Main.Data.Contexts;
using Main.Entities;

namespace FinalLab.Application.Handlers
{
    public class AddOrUpdateReactionCommandHandler : IRequestHandler<UpdateReactionCommand>
    {
        private readonly AppDbContext _context;

        public AddOrUpdateReactionCommandHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task Handle(UpdateReactionCommand request, CancellationToken cancellationToken)
        {
            var reaction = await _context.Reactions
                .FirstOrDefaultAsync(r => r.UserId == request.UserId && r.ArticleId == request.ArticleId, cancellationToken);

            if (reaction != null)
            {
                // Update existing reaction
                reaction.ReactionType = request.ReactionType;
                reaction.IsFlagged = request.IsFlagged;
            }
            else
            {
                // Add new reaction
                reaction = new Reaction
                {
                    UserId = request.UserId,
                    ArticleId = request.ArticleId,
                    ReactionType = request.ReactionType,
                    IsFlagged = request.IsFlagged
                };
                _context.Reactions.Add(reaction);
            }

            await _context.SaveChangesAsync(cancellationToken);

        }
    }
}