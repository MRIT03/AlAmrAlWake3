using System;
using System.Text.Json.Serialization;

public class ArticleDto
{
    [JsonPropertyName("articleId")]
    public int ArticleId { get; set; }

    [JsonPropertyName("headline")]
    public string Headline { get; set; }

    [JsonPropertyName("body")]
    public string Body { get; set; }

    [JsonPropertyName("timeCreated")]
    public DateTime TimeCreated { get; set; }

    [JsonPropertyName("pts")]
    public double Pts { get; set; }

    [JsonPropertyName("sourceId")]
    public int SourceId { get; set; }
}