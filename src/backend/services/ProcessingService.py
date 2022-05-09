class ProcessingService:
    @staticmethod
    def positive_percentage(comments: []):
        number_of_comments = len(comments)
        filter_positive_comments = len([comment for comment in comments if comment.Ai_FeedBack == 1])
        return 0 if number_of_comments == 0 else int((filter_positive_comments / number_of_comments) * 100)

    @staticmethod
    def not_logic(value: int):
        print("value")
        print(value)
        return 1 if value == 0 else 0

    @staticmethod
    def get_user_feedback(ai_feedback: int, user_ia_feedback):
        print (user_ia_feedback)
        return ProcessingService.not_logic(ai_feedback) if int(user_ia_feedback) == 0 else int(ai_feedback)



