using Microsoft.AspNetCore.Mvc;

namespace Main.Controllers;

public class SpaController : Controller
{
    [HttpGet]
    public IActionResult Index()
    {
        // points to wwwroot/app/index.html
        var file = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "app", "index.html");
        return PhysicalFile(file, "text/html");
    }
}