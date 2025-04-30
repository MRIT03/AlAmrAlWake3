using FinalLab.Application.Commands;
using MediatR;
using Microsoft.EntityFrameworkCore;
using System.Threading;
using System.Threading.Tasks;
using Main.Data.Contexts;

namespace FinalLab.Application.Handlers
{
    public class UpdateUserInfoCommandHandler : IRequestHandler<UpdateUserInfoCommand>
    {
        private readonly AppDbContext _context;

        public UpdateUserInfoCommandHandler(AppDbContext context)
        {
            _context = context;
        }

        public async Task Handle(UpdateUserInfoCommand request, CancellationToken cancellationToken)
        {
            var user = await _context.Users
                .FirstOrDefaultAsync(u => u.UserId == request.UserId, cancellationToken);

            if (user != null)
            {
                // Update the user's information
                user.Username = request.Username;
                user.EmailAddress = request.EmailAddress;
                await _context.SaveChangesAsync(cancellationToken);
            }

        }
    }
}
