using Main.Commands;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Threading;
using System.Threading.Tasks;
using Main.Commands;
using Main.Data.Contexts;

namespace Main.Handlers
{
    public class LabelPostCommandHandler : IRequestHandler<LabelPostCommand>
    {
        private readonly AppDbContext _context;

        public LabelPostCommandHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task Handle(LabelPostCommand request, CancellationToken cancellationToken)
        {
            var article = await _context.Articles
                .FirstOrDefaultAsync(a => a.ArticleId == request.ArticleId, cancellationToken);

            if (article != null)
            {
                // Update the label of the article
                article.Headline = request.Label;
                await _context.SaveChangesAsync(cancellationToken);
            }

        }
    }
}
