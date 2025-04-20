using System.ComponentModel.DataAnnotations;

namespace Main.Entities;

public class Region
{
    [Key]
    public int RegionId { get; set; }

    [Required, MaxLength(100)]
    public string RegionName { get; set; }

    [MaxLength(100)]
    public string District { get; set; }

    public double Latitude { get; set; }
    public double Longitude { get; set; }

    public ICollection<User> Users { get; set; }
    public ICollection<Article> Articles { get; set; }
}