import openai
from app.config import ALICE_API_KEY, ALICE_FOLDER_ID, ALICE_MODEL_URI
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.prompts.context import BUSINESS_CONTEXT

client = openai.OpenAI(
    api_key=ALICE_API_KEY,
    base_url="https://ai.api.cloud.yandex.net/v1",
    project=ALICE_FOLDER_ID,
)


class LLMService:
    def _build_input(self, history: list, user_text: str) -> str:
        lines = []
        for item in history:
            role = "Стажёр" if item["role"] == "user" else "HelpJunior"
            lines.append(f"{role}: {item['text']}")
        lines.append(f"Стажёр: {user_text}")
        return "\n".join(lines)

    def ask(self, history: list, user_text: str) -> str:
        try:
            full_instructions = f"{SYSTEM_PROMPT}\n\n{BUSINESS_CONTEXT}"
            response = client.responses.create(
                model=f"gpt://{ALICE_FOLDER_ID}/{ALICE_MODEL_URI}",
                temperature=0.3,
                instructions=full_instructions
                input=self._build_input(history, user_text),
                max_output_tokens=1500,
            )
            return response.output_text
        except openai.AuthenticationError as e:
            return f"Ошибка авторизации Alice AI LLM: проверьте API-ключ и folder ID. {e}"
        except openai.APIError as e:
            return f"Ошибка обращения к Alice AI LLM: {e}"