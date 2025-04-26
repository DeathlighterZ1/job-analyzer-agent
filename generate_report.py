def create_feedback_report(feedback, score):
    report = f"""
    JOB ANALYZER REPORT
    ---------------------
    Score: {score}/100

    Detailed Feedback:
    {feedback}
    """
    return report
