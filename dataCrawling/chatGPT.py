import openai


def chatGPT(ask):
    openai.api_key = ''
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=ask,
      max_tokens=50,
      temperature = 0.5
    )
    return response.choices[0].text.strip()
def chatGPTTurbo(ask):
    openai.api_key = ''
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "user", "content": ask},
        ]
    )
    output_text = response["choices"][0]["message"]["content"]
    return output_text


if __name__ == '__main__':
  print(chatGPT('안녕 반가워'))
  