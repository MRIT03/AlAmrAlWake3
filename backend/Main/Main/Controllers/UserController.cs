using System.Collections.Generic;
using System.Threading.Tasks;
using Main.Data.Contexts;
using Main.Entities;
using Microsoft.AspNetCore.Http.HttpResults;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;


namespace Main.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class UserController : ControllerBase
    {
        private readonly AppDbContext _context;

        public UserController(AppDbContext context)
        {
            _context = context;
        }

        // GET: /api/FollowsSource
        [HttpGet("[action]")]
        public ActionResult<Boolean> FollowsSource([FromQuery] int userId, [FromQuery] int sourceId)
        {
            var follow = _context.Follows.Where(f => f.UserId == userId && f.SourceId == sourceId).ToList();
            if (follow.Count == 0)
            {
                return Ok(false);
            }
            return Ok(true);
        }

        [HttpPost("[action]")]
        public ActionResult<Boolean> Follow([FromQuery] int userId, [FromQuery] int sourceId)
        {
            var follow = _context.Follows.Where(f => f.UserId == userId && f.SourceId == sourceId).ToList();
            if (follow.Count == 0)
            {
                Follow followEntity = new Follow()
                {
                    UserId = userId,
                    SourceId = sourceId,
                    FollowDate = DateTime.Now
                };
                _context.Follows.Add(followEntity);
                _context.SaveChanges();
                return Ok(true);
            }
            return BadRequest();
        }
    }
}