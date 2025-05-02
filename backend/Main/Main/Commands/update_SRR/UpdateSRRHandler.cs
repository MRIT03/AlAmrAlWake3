using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Main.Data.Contexts;
using Main.Commands;
using System;

namespace Main.Handlers
{
    public class ComputeSRRCommandHandler : IRequestHandler<UpdateSRRCommand>
    {
        private readonly AppDbContext _context;

        public ComputeSRRCommandHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task Handle(UpdateSRRCommand request, CancellationToken cancellationToken)
        {
            // Fetch articles by the source
            var articles = await _context.Articles
                .Where(a => a.SourceId == request.SourceId)
                .ToListAsync(cancellationToken);

            // If no articles found, return without updating SRR
            if (!articles.Any())
            {
                return;
            }

            // Fetch the PTS of each article (assuming PTS is already calculated and stored)
            var totalPTS = articles.Sum(a => a.PTS);
            var P = articles.Count;

            // Calculate SRR
            var SRR = (1.0 / P) * (totalPTS / 20.0);

            // Update the SRR of the source
            var source = await _context.Sources
                .FirstOrDefaultAsync(s => s.SourceId == request.SourceId, cancellationToken);

            if (source != null)
            {
                source.SRR = SRR;
                await _context.SaveChangesAsync(cancellationToken);
            }
        }
    }
}
