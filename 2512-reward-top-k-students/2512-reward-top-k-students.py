from collections import defaultdict

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        feedbacks = dict()
        for i in student_id:
            feedbacks[i] = 0
        
        for idx, sid in enumerate(student_id):
            feedback = report[idx].split() 
            for word in feedback:
                if word in positive_feedback:
                    feedbacks[sid] += 3
                elif word in negative_feedback:
                    feedbacks[sid] -= 1

        result = sorted(feedbacks.items(), key=lambda x: (-x[1], x[0]))

        return [sid for sid, _ in result[:k]]
        