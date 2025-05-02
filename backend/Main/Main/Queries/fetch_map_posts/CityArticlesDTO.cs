namespace Main.Queries.DTO
{
    public class CityArticlesDto
    {
        public string City { get; set; }
        public List<double> Coordinates { get; set; }
        public List<ArticleDto> Articles { get; set; }
    }

    
}
