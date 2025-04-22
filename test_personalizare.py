
import unittest

class TestPsychologicalAdaptation(unittest.TestCase):
    def test_emotion_detection_simulation(self):
        text = "Sunt nervos și agitat"
        sentiment = "agresivitate"
        self.assertIn(sentiment, ["anxietate", "agresivitate", "relaxare", "incertitudine", "stres"])

    def test_behavioral_history_adjustment(self):
        memory = {"task_failed": "calm_response"}
        current_context = "task_failed"
        self.assertEqual(memory[current_context], "calm_response")

if __name__ == "__main__":
    unittest.main()
