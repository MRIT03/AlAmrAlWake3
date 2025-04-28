namespace FinalLab.Application.DTOs
{
    public class CityArticlesDto
    {
        public string City { get; set; }
        public List<double> Coordinates { get; set; }
        public List<ArticleDto> Articles { get; set; }
    }

    public class ArticleDto
    {
        public long ArticleId { get; set; }
        public string Headline { get; set; }
    }
}
