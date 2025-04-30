using FinalLab.Application.Commands;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Threading;
using System.Threading.Tasks;
using Main.Commands;
using Main.Data.Contexts;

namespace Main.Handlers
{
    public class DeleteArticleCommandHandler : IRequestHandler<DeleteArticleCommand>
    {
        private readonly AppDbContext _context;

        public DeleteArticleCommandHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task Handle(DeleteArticleCommand request, CancellationToken cancellationToken)
        {
            var article = await _context.Articles
                .FirstOrDefaultAsync(a => a.ArticleId == request.ArticleId, cancellationToken);

            if (article != null)
            {
                // Delete the article
                _context.Articles.Remove(article);
                await _context.SaveChangesAsync(cancellationToken);
            }

        }
    }
}
