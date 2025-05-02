namespace Main.Queries.DTO
{
    public class PostInfoDto
    {
        public string City { get; set; }
        public string SelectedReaction { get; set; }
        public List<int> Counters { get; set; }
        public string Headline { get; set; }
        public string Body { get; set; }
        public string SourceName { get; set; }
        public double SRR { get; set; }
        public double PTS { get; set; }
        public DateTime DateTime { get; set; }
        public string IsAdmin { get; set; }
        public DateTime TimeCreated { get; set; }
        public int ArticleId { get; set; }
    }
}
