from resourses import openai_client


def get_answer_from_gpt(message: str) -> str:
    response = openai_client.chat.completions.create(
        model='ft:gpt-3.5-turbo-0613:alex-maison::8MDSu2t4',
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    answer = response.choices[0].message.content
    return answer
