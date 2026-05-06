def evaluate_answer(answer, expected_keywords):
    answer = answer.lower()
    matched = []

    for keyword in expected_keywords:
        if keyword.lower() in answer:
            matched.append(keyword)

    score = int((len(matched) / len(expected_keywords)) * 10)

    missing = [k for k in expected_keywords if k not in matched]

    feedback = f"Matched keywords: {', '.join(matched)}. "
    if missing:
        feedback += f"Missing keywords: {', '.join(missing)}."
    else:
        feedback += "Excellent answer."

    return score, feedback