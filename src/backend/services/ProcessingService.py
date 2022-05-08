class ProcessingService:
    @staticmethod
    def positive_percentage(comments: []):
        number_of_comments = len(comments)
        filter_positive_comments = len([comment for comment in comments if comment.Ai_FeedBack == 1])
        return 0 if number_of_comments == 0 else int((filter_positive_comments / number_of_comments) * 100)
