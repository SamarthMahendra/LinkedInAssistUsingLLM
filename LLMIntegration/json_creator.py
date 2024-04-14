from openai import OpenAI


class JobFilterAssistant:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def filter_jobs(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """You are a helpful assistant who takes natural language questions 
                               and helps user filter LinkedIn job postings by returning filter 
                               "JSON format\n\nJob title goes under: keywords\nLocation goes under: location
                               time period in seconds goes under: time_period\n\nFor example, 1 day = 86400
                               f_E=1 for intership f_E=2 for entry level f_E=3 for mid level f_E=4 for senior level
f_E=5 for director
f_E=6 for executive
for internship and entry level f_E=1,2 f_E is the key for experience level
salary 
f_SB2=1 for 40k +
f_SB2=2 for 60k +
f_SB2=3 for 80k +
f_SB2=4 for 100k + and so on dont give short forms of any values, try to give full values ex ca for california, pm for product manager etc"""

                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        assistant_response = response.choices[0].message.content
        print(assistant_response)
        return assistant_response
