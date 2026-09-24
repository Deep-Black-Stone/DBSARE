"""Dependency-free OpenAI-compatible HTTP adapter."""
import json
import os
from urllib.request import Request, urlopen
from ..llm import LLMRequest, LLMResponse

class OpenAICompatibleBackend:
    def __init__(self, base_url: str | None = None, api_key: str | None = None, model: str | None = None, timeout: int = 30):
        self.base_url = (base_url or os.getenv("DBSARE_LLM_BASE_URL", "")).rstrip("/")
        self.api_key = api_key or os.getenv("DBSARE_LLM_API_KEY", "")
        self.model = model or os.getenv("DBSARE_LLM_MODEL", "")
        self.timeout = timeout

    def generate(self, request: LLMRequest) -> LLMResponse:
        if not self.base_url or not self.model:
            raise RuntimeError("LLM backend is not configured.")
        payload = {"model": self.model, "messages": [{"role":"system","content":request.system},{"role":"user","content":request.prompt}]}
        headers = {"Content-Type":"application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        req = Request(self.base_url + "/chat/completions", data=json.dumps(payload).encode(), headers=headers, method="POST")
        with urlopen(req, timeout=self.timeout) as response:
            data=json.load(response)
        text=data["choices"][0]["message"]["content"]
        return LLMResponse(text=text, model=self.model, metadata={"provider":"openai-compatible"})
