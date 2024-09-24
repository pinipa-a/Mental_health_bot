from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List

# Actions for anxiety response
class ActionAnxietyResponse(Action):
    def name(self) -> Text:
        return "action_anxiety_response"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="I'm sorry to hear that you're feeling anxious. Talking to someone or writing about your feelings might help.")
        return []

# Actions for writing journal
class ActionJournal(Action):
    def name(self) -> Text:
        return "action_journal"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        journal_entry = tracker.get_slot('journal_entry')
        if journal_entry:
            dispatcher.utter_message(text="Thank you for sharing your journal entry. Remember, it's important to express your feelings.")
        else:
            dispatcher.utter_message(text="It seems like you didn't provide any journal entry. Feel free to try again.")
        return []

# Actions for emegency help
class ActionEmergencyHelp(Action):
    def name(self) -> Text:
        return "action_emergency_help"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="If you're in immediate danger, please contact emergency services or seek help from a mental health professional.")
        return []

# Actions for giving selfcare tips
class ActionSelfCareTips(Action):
    def name(self) -> Text:
        return "action_self_care_tips"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Here are some self-care tips:\n\n1. Take regular breaks.\n2. Meditate for a few minutes each day.\n3. Spend time in nature.\n4. Get enough sleep.\n5. Stay hydrated and eat well.")
        return []


# Actions for track mood
class ActionTrackMood(Action):
    def name(self) -> Text:
        return "action_track_mood"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Tracking your mood helps in managing your mental health. Thank you for sharing!")
        return []

# Actions for guided breathing exercise
class ActionGuidedBreathing(Action):
    def name(self) -> Text:
        return "action_guided_breathing"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Let's start with some deep breathing. Breathe in... and breathe out. Continue for a few moments.")
        return []


class ActionContinueBreathing(Action):
    def name(self) -> Text:
        return "action_continue_breathing"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Keep breathing deeply. Focus on your breath and relax.")
        return []

class ActionEndBreathing(Action):
    def name(self) -> Text:
        return "action_end_breathing"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Well done! You can open your eyes and continue with your day.")
        return []

# Actions for ending conversation
class ActionGoodbye(Action):
    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Goodbye! Take care and feel free to reach out whenever you need help.")
        return []