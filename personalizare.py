
import logging

logger = logging.getLogger(__name__)

class PsychologicalAdapter:
    def __init__(self):
        self.memory = {}

    def detect_emotion(self, text_input):
        simulated_result = "agresivitate" if "nervos" in text_input else "neutru"
        logger.info(f"[Emotion] Emoție detectată: {simulated_result}")
        return simulated_result

    def adjust_response(self, context_key):
        return self.memory.get(context_key, "default_response")

    def update_behavior_memory(self, key, value):
        self.memory[key] = value
        logger.info(f"[Behavior] Memorare reacție: {key} -> {value}")
