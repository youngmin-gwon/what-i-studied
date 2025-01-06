---
title: gemini curl
tags: [ai]
aliases: []
date modified: 2025-01-06 09:45:36 +09:00
date created: 2025-01-06 09:32:58 +09:00
---

## Prerequisites

```python
os.environ["PROJECT_ID"] = PROJECT_ID
os.environ["LOCATION"] = LOCATION
os.environ["API_ENDPOINT"] = f"{LOCATION}-aiplatform.googleapis.com">
os.environ["MODEL_ID"] = "gemini-1.5-pro"
```

## cURL commands

### Generate Contents

#### single response

```bash
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  https://${API_ENDPOINT}/v1/projects/${PROJECT_ID}/locations/${LOCATION}/publishers/google/models/${MODEL_ID}:generateContent \
  -d '{
    "contents": {
      "role": "USER",
      "parts": { "text": "Why is the sky blue?" }
    }
  }'

```

#### stream

```bash
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  https://${API_ENDPOINT}/v1/projects/${PROJECT_ID}/locations/${LOCATION}/publishers/google/models/${MODEL_ID}:streamGenerateContent \
  -d '{
    "contents": {
      "role": "USER",
      "parts": { "text": "Why is the sky blue?" }
    }
  }'
```

#### parameter configuration

```bash
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  https://${API_ENDPOINT}/v1/projects/${PROJECT_ID}/locations/${LOCATION}/publishers/google/models/${MODEL_ID}:generateContent \
  -d '{
    "contents": {
      "role": "USER",
      "parts": [
        {"text": "Describe this image"},
        {"file_data": {
          "mime_type": "image/png",
          "file_uri": "gs://cloud-samples-data/generative-ai/image/320px-Felis_catus-cat_on_snow.jpg"
        }}
      ]
    },
    "generation_config": {
      "temperature": 0.2,
      "top_p": 0.1,
      "top_k": 16,
      "max_output_tokens": 2048,
      "candidate_count": 1,
      "stop_sequences": []
    },
    "safety_settings": {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_LOW_AND_ABOVE"
    }
  }'
```

#### function calling

custom function 을 만들어 호출하는 방법

```bash
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  https://${API_ENDPOINT}/v1beta1/projects/${PROJECT_ID}/locations/${LOCATION}/publishers/google/models/${MODEL_ID}:generateContent \
  -d '{
  "contents": {
    "role": "user",
    "parts": {
      "text": "Which theaters in Mountain View show Barbie movie?"
    }
  },
  "tools": [
    {
      "function_declarations": [
        {
          "name": "find_movies",
          "description": "find movie titles currently playing in theaters based on any description, genre, title words, etc.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "description": {
                "type": "string",
                "description": "Any kind of description including category or genre, title words, attributes, etc."
              }
            },
            "required": [
              "description"
            ]
          }
        },
        {
          "name": "find_theaters",
          "description": "find theaters based on location and optionally movie title which are is currently playing in theaters",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "movie": {
                "type": "string",
                "description": "Any movie title"
              }
            },
            "required": [
              "location"
            ]
          }
        },
        {
          "name": "get_showtimes",
          "description": "Find the start times for movies playing in a specific theater",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616"
              },
              "movie": {
                "type": "string",
                "description": "Any movie title"
              },
              "theater": {
                "type": "string",
                "description": "Name of theater"
              },
              "date": {
                "type": "string",
                "description": "Date for requested showtime"
              }
            },
            "required": [
              "location",
              "movie",
              "theater",
              "date"
            ]
          }
        }
      ]
    }
  ]
}'
```

### Multi-modal input

#### Generate contents from image

#### local image

```bash
data=$(base64 -w 0 image.jpg)

curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  https://${API_ENDPOINT}/v1/projects/${PROJECT_ID}/locations/${LOCATION}/publishers/google/models/${MODEL_ID}:generateContent \
  -d "{
      'contents': {
        'role': 'USER',
        'parts': [
          {
            'text': 'Is it a cat?'
          },
          {
            'inline_data': {
              'data': '${data}',
              'mime_type':'image/jpeg'
            }
          }
        ]
       }
     }"
```

#### from google cloud

```bash
MODEL_ID="gemini-1.5-pro"

curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  https://${API_ENDPOINT}/v1/projects/${PROJECT_ID}/locations/${LOCATION}/publishers/google/models/${MODEL_ID}:generateContent \
  -d '{
    "contents": {
      "role": "USER",
      "parts": [
        {
          "text": "Describe this image"
        },
        {
          "file_data": {
            "mime_type": "image/png",
            "file_uri": "gs://cloud-samples-data/generative-ai/image/320px-Felis_catus-cat_on_snow.jpg"
          }
        }
      ]
    },
    "generation_config": {
      "temperature": 0.2,
      "top_p": 0.1,
      "top_k": 16,
      "max_output_tokens": 2048,
      "candidate_count": 1,
      "stop_sequences": []
    },
    "safety_settings": {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_LOW_AND_ABOVE"
    }
  }'
```

### Generate contents from video

```bash
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  https://${API_ENDPOINT}/v1/projects/${PROJECT_ID}/locations/${LOCATION}/publishers/google/models/${MODEL_ID}:generateContent \
  -d \
'{
    "contents": {
      "role": "USER",
      "parts": [
        {
          "text": "Answer the following questions using the video only. What is the profession of the main person? What are the main features of the phone highlighted?Which city was this recorded in?Provide the answer JSON."
        },
        {
          "file_data": {
            "mime_type": "video/mp4",
            "file_uri": "gs://github-repo/img/gemini/multimodality_usecases_overview/pixel8.mp4"
          }
        }
      ]
    }
  }'
```
