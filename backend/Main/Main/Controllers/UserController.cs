using System.Collections.Generic;
using System.Threading.Tasks;
using Main.Data.Contexts;
using Main.Entities;
using Microsoft.AspNetCore.Http.HttpResults;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Identity;


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

        [HttpPost("[action]")]
        public ActionResult SignUp([FromForm] UserFormDto userForm)
        {
            var username = _context.Users.SingleOrDefault(u => userForm.UserName == u.Username);
            if(username != null) return BadRequest("Username already taken");
            User newUser = new User()
            {
                Username = userForm.UserName,
                EmailAddress = userForm.EmailAddress,
                UserRole = userForm.UserRole,
                CreatedAt = DateTime.Now,
            };
            var hasher =new PasswordHasher<User>();
            newUser.HashedPassword = hasher.HashPassword(newUser, userForm.Password);
            var region = _context.Regions.Single(r => r.RegionName == userForm.Region).RegionId;
            newUser.RegionId = region;
            _context.Users.Add(newUser);
            _context.SaveChanges();
            return Ok();

        }

        [HttpPost("[action]")]
        public ActionResult<Boolean> Login([FromForm] LoginFormDto userForm)
        {
            var user = _context.Users.SingleOrDefault(u => userForm.Username == u.Username);
            if(user == null ) return BadRequest("Username doesn't exist");
            var hasher = new PasswordHasher<User>();
            var verify = hasher.VerifyHashedPassword(user, user.HashedPassword, userForm.Password);
            if (verify != PasswordVerificationResult.Success)
            {
                return BadRequest("Incorrect Username or Password");
            }
            else return Ok(true);
        }
    }

    public class UserFormDto
    {
        public string UserName { get; set; }
        public string EmailAddress { get; set; }
        public string Password { get; set; }
        public string UserRole { get; set; }
        public string Region { get; set; }
        
    }

    public class LoginFormDto
    {
        public string Username { get; set; }
        public string Password { get; set; }
    }
}