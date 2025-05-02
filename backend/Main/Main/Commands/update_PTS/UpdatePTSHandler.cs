using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Threading;
using System.Threading.Tasks;
using Main.Data.Contexts;
using Main.Commands;
using System;
using System.Linq;

namespace Main.Handlers
{
    public class UpdatePTSHandler : IRequestHandler<UpdatePTSCommand>
    {
        private readonly AppDbContext _context;

        public UpdatePTSHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task Handle(UpdatePTSCommand request, CancellationToken cancellationToken)
        {
            const double k = 1.0;

            var reactions = _context.Reactions
                .Where(r => r.ArticleId == request.ArticleId);

            var Nf = await reactions.CountAsync(r => r.IsFlagged, cancellationToken);
            var Ni = await reactions.CountAsync(cancellationToken);

            var penalty = Math.Min(1.0, k * Nf / (Ni + 1));
            var pts = 100.0 * (1.0 - penalty);

            var article = await _context.Articles
                .FirstOrDefaultAsync(a => a.ArticleId == request.ArticleId, cancellationToken);

            if (article != null)
            {
                article.PTS = pts;
                await _context.SaveChangesAsync(cancellationToken);
            }
        }
    }
}
