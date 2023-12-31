from box import Box
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage

from assistant.constants import OPENAI_API_KEY, OPENAI_ORGANIZATION
import os

class LanguageModel:
    def __init__(self, config: Box):
        """Initialize LLM."""
        self.client = OpenAI(
            api_key=os.getenv(OPENAI_API_KEY),
            organization=os.getenv(OPENAI_ORGANIZATION),
        )
        self.history: list[dict] = [] # Not used yet :)
        self.extra_instructions = config.language_model.extra_instructions
        self.model = config.language_model.model
    
    def answer_prompt(
        self,
        system_prompt: str | None,
        user_prompt: str,
        use_extra_instructions: bool = True,
    ) -> ChatCompletionMessage:
        """Answer prompt."""

        system_prompt = (
            system_prompt 
            if system_prompt
            else "You are a helpful assistant."
        )
        if use_extra_instructions:
            system_prompt += " " + self.extra_instructions
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {"role": "user", "content": user_prompt},
            ],
        )
        return completion.choices[0].message