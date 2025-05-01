using System.Collections.Generic;
using System.Threading.Tasks;
using Main.Data.Contexts;
using Main.Entities;
using Main.Queries;
using Main.Queries.DTO;
using MediatR;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;


namespace Main.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class PostsController : ControllerBase
    {
        private readonly AppDbContext _context;
        private readonly IMediator _mediator;

        public PostsController(AppDbContext context, IMediator mediator)
        {
            _context = context;
            _mediator = mediator;
        }

        // GET: /api/posts
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Article>>> GetPosts()
        {
            var posts = await _context.Articles.ToListAsync();
            return Ok(posts);
        }

        [HttpGet("[action]")]
        public async Task<ActionResult<List<CityArticlesDto>>> GetMapPosts()
        {
            var res = await _mediator.Send(new FetchHeadlinesQuery());
            
            if (res != null) return Ok(res);
            return NoContent();
            
        }
        
        [HttpGet("[action]")]
        public async Task<ActionResult<List<CityArticlesDto>>> GetFeedPosts()
        {
            var res = await _mediator.Send(new FetchFeedPostsQuery(2));
            
            if (res != null) return Ok(res);
            return NoContent();
            
        }
    }
}