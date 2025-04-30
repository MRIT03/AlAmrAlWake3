using MediatR;

namespace FinalLab.Application.Commands
{
    public class UpdateUserInfoCommand : IRequest
    {
        public int UserId { get; }
        public string Username { get; }
        public string EmailAddress { get; }

        public UpdateUserInfoCommand(int userId, string username, string emailAddress)
        {
            UserId = userId;
            Username = username;
            EmailAddress = emailAddress;
        }
    }
}
