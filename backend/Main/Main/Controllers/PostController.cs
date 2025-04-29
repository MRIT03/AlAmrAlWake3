using System.Collections.Generic;
using System.Threading.Tasks;
using Main.Data.Contexts;
using Main.Entities;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;


namespace Main.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class PostsController : ControllerBase
    {
        private readonly AppDbContext _context;

        public PostsController(AppDbContext context)
        {
            _context = context;
        }

        // GET: /api/posts
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Article>>> GetPosts()
        {
            var posts = await _context.Articles.ToListAsync();
            return Ok(posts);
        }
    }
}