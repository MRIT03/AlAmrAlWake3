using Main.Entities;
using Microsoft.EntityFrameworkCore;

namespace Main.Data.Contexts;

public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options)
        : base(options) { }

    public DbSet<User> Users { get; set; }
    public DbSet<Source> Sources { get; set; }
    public DbSet<Region> Regions { get; set; }
    public DbSet<Article> Articles { get; set; }
    public DbSet<Follow> Follows { get; set; }
    public DbSet<Reaction> Reactions { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // Configure table names if needed
        modelBuilder.Entity<Follow>()
            .HasOne(f => f.User)
            .WithMany(u => u.Follows)
            .HasForeignKey(f => f.UserId);

        modelBuilder.Entity<Follow>()
            .HasOne(f => f.Source)
            .WithMany(s => s.Followers)
            .HasForeignKey(f => f.SourceId);

        modelBuilder.Entity<Reaction>()
            .HasOne(r => r.User)
            .WithMany(u => u.Reactions)
            .HasForeignKey(r => r.UserId);

        modelBuilder.Entity<Reaction>()
            .HasOne(r => r.Article)
            .WithMany(a => a.Reactions)
            .HasForeignKey(r => r.ArticleId);
    }
}