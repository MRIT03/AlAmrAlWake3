using FinalLab.Application.Commands;
using FinalLab.Infrastructure.Persistence;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Threading;
using System.Threading.Tasks;

namespace FinalLab.Application.Handlers
{
    public class DeleteArticleCommandHandler : IRequestHandler<DeleteArticleCommand>
    {
        private readonly AppDbContext _context;

        public DeleteArticleCommandHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task<Unit> Handle(DeleteArticleCommand request, CancellationToken cancellationToken)
        {
            var article = await _context.ARTICLE
                .FirstOrDefaultAsync(a => a.ArticleId == request.ArticleId, cancellationToken);

            if (article != null)
            {
                // Delete the article
                _context.ARTICLE.Remove(article);
                await _context.SaveChangesAsync(cancellationToken);
            }

            return Unit.Value;
        }
    }
}
