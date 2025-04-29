using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Main.Entities;

public class Follow
{
    [Key]
    public int FollowId { get; set; }

    [Column(TypeName = "date")]
    public DateTime FollowDate { get; set; }

    // Foreign keys
    public int UserId { get; set; }
    public User User { get; set; }

    public int SourceId { get; set; }
    public Source Source { get; set; }
}