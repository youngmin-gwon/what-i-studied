---
title: prompt_engineering
tags: []
aliases: []
date modified: 2024-12-24 00:45:06 +09:00
date created: 2024-12-22 19:35:50 +09:00
---

## Tips

### 간결하게 작성하기 (Be Concise)

너무 불필요하게 부연설명을 많이 적지 말자. 명령형으로 작성하기.

before

```plaintext
What do you think could be a good name for a flower shop that specializes in selling bouquets of dried flowers more than fresh flowers?
```

after

```plaintext
Suggest a name for a flower shop that sells bouquets of dried flowers
```

### 구체적이고 명확하게 정의하기 (Be specific, and well-defined)

before

```plaintext
Tell me about Earth
```

after

```plaintext
Generate a list of ways that makes Earth unique compared to other planets
```

### 한 번에 하나의 작업만 요청하기

before

```plaintext
What's the best method of boiling water and why is the sky blue?
```

after

```plaintext
What's the best method of boiling water?
```

### Hallucinations 제거

#### 시스템 명령 제공하여 무관한 답변 내놓는것 막기

[Google Vertex AI system instructions](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-chat-prompts-gemini#system-instructions)

```python
system_instructions=[
    "Hello! You are an AI chatbot for a travel web site.",
    "Your mission is to provide helpful queries for travelers.",
    "Remember that before you answer a question, you must check to see if it complies with your mission.",
    "If not, you can say, Sorry I can't answer that question.",
]
```

### 생성 작업 대신 분류 작업 요청하기

생성 작업을 요청하면 브레인스토밍에 좋지만, 답변은 변동이 심함

```plaintext
I'm a high school student. Which of these activities do you suggest and why:

a. learn Python
b. learn JavaScript
c. learn Fortran
```

### 예시를 포함하여 대답 품질 개선하기

지나치게 많은 예시는 과적합을 유발할 수 있고 답변 품질을 떨어트림

#### Zero-shot prompt

질문 안에 아무른 예시도 제공하지 않은 프롬프트

다른 프롬프트 보다 창의적인 답변을 얻을 수 있음

하지만 일관적이지 않을 수 있음

```python
prompt = """Decide whether a Tweet's sentiment is positive, neutral, or negative.

Tweet: I loved the new YouTube video you made!
Sentiment:
"""

print(call_gemini(prompt)) # Sentiment: **Positive**
```

#### One-shot prompt

원하는 답변 종류를 알려주기 위해 하나의 예시를 제공한 프롬프트

Zero-shot 보다 일관된 답을 얻을 수 있음

```python
prompt = """Decide whether a Tweet's sentiment is positive, neutral, or negative.

Tweet: I loved the new YouTube video you made!
Sentiment: positive

Tweet: That was awful. Super boring 😠
Sentiment:
"""

print(call_gemini(prompt)) # Sentiment: **negative**
```

#### Few-shot prompt

원하는 답변 종류를 알려주기 위해 몇개의 예시를 제공한 프롬프트

```python
prompt = """Decide whether a Tweet's sentiment is positive, neutral, or negative.

Tweet: I loved the new YouTube video you made!
Sentiment: positive

Tweet: That was awful. Super boring 😠
Sentiment: negative

Tweet: Something surprised me about this video - it was actually original. It was not the same old recycled stuff that I always see. Watch it - you will not regret it.
Sentiment:
"""

print(call_gemini(prompt))

# Sentiment: **positive**

# Here's why:

# * **"Something surprised me about this video - it was actually original"** indicates a positive surprise.
# * **"It was not the same old recycled stuff"** further reinforces the positive sentiment.
# * **"Watch it - you will not regret it"** is a strong recommendation, further confirming a positive view.
```
