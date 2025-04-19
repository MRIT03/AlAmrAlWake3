using System.ComponentModel.DataAnnotations;

namespace Main.Entities;

public class Article
{
    [Key]
    public int ArticleId { get; set; }

    public DateTime TimeCreated { get; set; }

    [Required]
    public string Headline { get; set; }

    public string Body { get; set; }

    public int PTS { get; set; }

    // Foreign keys
    public int SourceId { get; set; }
    public Source Source { get; set; }

    public int RegionId { get; set; }
    public Region Region { get; set; }

    public ICollection<Reaction> Reactions { get; set; }
}