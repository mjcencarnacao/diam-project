from .AIService import AIService
from home.models import Comments

class ProcessingService:
    @staticmethod
    def positive_percentage(comments: []):
        number_of_comments = len(comments)
        filter_positive_comments = len([comment for comment in comments if comment.AI_FeedBack == 1])
        return 0 if number_of_comments == 0 else int((filter_positive_comments / number_of_comments) * 100)

    @staticmethod
    def logic_gate_not(value: int):
        return 1 if value == 0 else 0

    @staticmethod
    def get_user_feedback(ai_feedback: int, user_ia_feedback):
        return ProcessingService.logic_gate_not(ai_feedback) if int(user_ia_feedback) == 0 else int(ai_feedback)

    @staticmethod
    def retrain_AI_with_user_feedback(id_comment: int, user_appreciation: int):
        ai_service: AIService = AIService()
        comment_object: Comments = Comments.objects.get(pk=id_comment)
        comment = comment_object.comment
        ai_comment_feedback = comment_object.AI_FeedBack
        user_feedback: int = ProcessingService.get_user_feedback(ai_comment_feedback, user_appreciation)
        ai_service.train_and_serialize(comment, user_feedback)
        ai_feedback, neg, pos = ai_service.classify(comment)
        comment_object.AI_FeedBack = ai_feedback
        ai_feedback_plain_text = ai_service.get_comment_plaintext(ai_feedback)
        comment_object.AI_Probability_PositiveFeedBack = pos
        comment_object.AI_Probability_NegativeFeedBack = neg
        comment_object.critic_feedback = True
        comment_object.save()
        return ai_feedback_plain_text



