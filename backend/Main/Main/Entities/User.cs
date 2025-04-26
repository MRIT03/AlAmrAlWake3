using System.ComponentModel.DataAnnotations;

namespace Main.Entities;

public class User
{
    [Key]
    public int UserId { get; set; }

    [Required, MaxLength(100)]
    public string Username { get; set; }

    [Required]
    public string HashedPassword { get; set; }

    [Required, EmailAddress]
    public string EmailAddress { get; set; }

    public DateTime CreatedAt { get; set; }

    [MaxLength(50)]
    public string UserRole { get; set; }

    // Foreign key to Region
    public int RegionId { get; set; }
    public Region Region { get; set; }

    public ICollection<Follow> Follows { get; set; }
    public ICollection<Reaction> Reactions { get; set; }
}