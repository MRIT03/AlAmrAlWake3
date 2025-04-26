using System.ComponentModel.DataAnnotations;

namespace Main.Entities;

public class Source
{
    [Key]
    public int SourceId { get; set; }

    [Required, MaxLength(200)]
    public string SourceName { get; set; }

    [Url]
    public string WebsiteURL { get; set; }

    public string RSS { get; set; }

    public ICollection<Article> Articles { get; set; }
    public ICollection<Follow> Followers { get; set; }
}