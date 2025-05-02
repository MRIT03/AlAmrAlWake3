using MediatR;

namespace Main.Commands
{
    public class UpdateSRRCommand : IRequest
    {
        public int SourceId { get; set; }

        public UpdateSRRCommand(int sourceId)
        {
            SourceId = sourceId;
        }
    }
}
