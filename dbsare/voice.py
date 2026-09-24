"""Voice interface contract; STT/TTS remain replaceable adapters."""
from dataclasses import dataclass

@dataclass(frozen=True)
class VoiceCommand:
    text: str
    confidence: float | None = None

class VoiceInterface:
    def accept_transcript(self, command: VoiceCommand) -> str:
        return command.text
