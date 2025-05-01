using System.IO;
using System.Reflection;
using Main.Data.Contexts;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.FileProviders;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllersWithViews();
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseNpgsql(builder.Configuration.GetConnectionString("DefaultConnection")));
builder.Services.AddMediatR(cfg => cfg.RegisterServicesFromAssembly(Assembly.GetExecutingAssembly()));

var app = builder.Build();

if (app.Environment.IsDevelopment())
    app.UseDeveloperExceptionPage();

app.UseHttpsRedirection();

// 1) Serve files in wwwroot/*
app.UseStaticFiles();

// 2) Also serve files in wwwroot/app at the same URL space
app.UseStaticFiles(new StaticFileOptions
{
    FileProvider = new PhysicalFileProvider(
        Path.Combine(app.Environment.WebRootPath, "app")),
    RequestPath = ""    // means “/index-xxx.js” will look in wwwroot/app/index-xxx.js
});

app.UseRouting();

app.MapControllerRoute(
    name: "api",
    pattern: "api/{controller}/{action=Index}/{id?}");

// fallback for SPA:
app.MapFallbackToFile("app/index.html");

app.Run();