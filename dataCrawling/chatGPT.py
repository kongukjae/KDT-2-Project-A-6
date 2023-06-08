import openai

openai.api_key = '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'

def chatGPT(ask):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=ask,
      max_tokens=70
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
  print(chatGPT('안녕 반가워'))