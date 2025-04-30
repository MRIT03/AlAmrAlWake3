using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Main.Entities;

public class Reaction
{
    [Key]
    public int ReactionId { get; set; }

    [Column(TypeName = "time")]
    public TimeSpan ReactionTime { get; set; }

    [Column(TypeName = "date")]
    public DateTime ReactionDate { get; set; }

    [Required, MaxLength(50)]
    public string ReactionType { get; set; }
    public bool IsFlagged { get; set; }

    // Foreign keys
    public int UserId { get; set; }
    public User User { get; set; }

    public int ArticleId { get; set; }
    public Article Article { get; set; }
}