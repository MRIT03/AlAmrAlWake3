using System.Collections.Generic;
using System.Threading.Tasks;
using Main.Data.Contexts;
using Main.Entities;
using MediatR;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;


namespace Main.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ReactionsController : ControllerBase
    {
        private readonly AppDbContext _context;
        private readonly IMediator _mediator;

        public ReactionsController(AppDbContext context, IMediator mediator)
        {
            _context = context;
            _mediator = mediator;
        }

        [HttpGet("[action]")]
        public async Task<ActionResult<List<Reaction>>> GetReactions([FromQuery] int userId, [FromQuery] int PostId)
        {
            var reactions = await _context.Reactions.Where(r => r.UserId == userId && r.ArticleId == PostId).ToListAsync();
            if(reactions!=null) return Ok(reactions);
            return NoContent();
        }

        [HttpPost("[action]")]
        public ActionResult UpdateReaction([FromQuery] ReactionDto reaction)
        {
            var userReaction = _context.Reactions.Single(r => r.UserId == reaction.UserId 
                                                              && r.ArticleId == reaction.ArticleId 
                                                              && r.IsFlagged == reaction.IsFlagged);
            if (userReaction == null)
            {
                Reaction newReaction = new Reaction()
                {
                    UserId = reaction.UserId,
                    ArticleId = reaction.ArticleId,
                    IsFlagged = reaction.IsFlagged,
                    ReactionDate = DateTime.Now
                };
                newReaction.ReactionType = newReaction.IsFlagged ? "flag":newReaction.ReactionType;
                _context.Reactions.Add(newReaction);
            }
            else
            {
                userReaction.ReactionType = reaction.ReactionType;
            }
            _context.SaveChanges();
            return Ok();
        }

        [HttpGet("[action]")]
        public ActionResult<ReactionCounters> CalculateReactions([FromQuery] int postId)
        {
            var reactions = _context.Reactions
                .Where(r => r.ArticleId == postId)
                .ToList();

            var counter = new ReactionCounters();

            foreach (var reaction in reactions)
            {
                if (reaction.IsFlagged)
                {
                    counter.Flag++;
                    continue;   
                }
                switch (reaction.ReactionType?.ToLowerInvariant())
                {
                    case "like":
                        counter.Like++;
                        break;
                    case "love":
                        counter.Love++;
                        break;
                    case "wow":
                        counter.Wow++;
                        break;
                    case "insightful":
                        counter.Insightful++;
                        break;
                    case "sad":
                        counter.Sad++;
                        break;
                    case "angry":
                        counter.Angry++;
                        break;
                    default:
                        // unknown or null reaction type: ignore
                        break;
                }
            }

            return Ok(counter);
        }
    }

    public class ReactionDto
    {
        public string ReactionType { get; set; }
        public int UserId { get; set; }
        public int ArticleId { get; set; }
        public bool IsFlagged { get; set; }
    }

    public class ReactionCounters
    {
        public int Like { get; set; }
        public int Love { get; set; }
        public int Flag { get; set; }
        public int Wow { get; set; }
        public int Insightful { get; set; }
        public int Sad { get; set; }
        public int Angry { get; set; }
    }
}

