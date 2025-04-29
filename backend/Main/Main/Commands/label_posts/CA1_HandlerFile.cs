using FinalLab.Application.Commands;
using FinalLab.Infrastructure.Persistence;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Threading;
using System.Threading.Tasks;

namespace FinalLab.Application.Handlers
{
    public class LabelPostCommandHandler : IRequestHandler<LabelPostCommand>
    {
        private readonly AppDbContext _context;

        public LabelPostCommandHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task<Unit> Handle(LabelPostCommand request, CancellationToken cancellationToken)
        {
            var article = await _context.ARTICLE
                .FirstOrDefaultAsync(a => a.ArticleId == request.ArticleId, cancellationToken);

            if (article != null)
            {
                // Update the label of the article
                article.Label = request.Label;
                await _context.SaveChangesAsync(cancellationToken);
            }

            return Unit.Value;
        }
    }
}
