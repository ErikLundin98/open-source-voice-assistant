from enum import Enum, auto
from box import Box

from assistant.language_model.model import LanguageModel
from assistant.language_model.tools import answer_question, get_weather, light_control, music_control

class Action(Enum):
    """List of actions."""
    NO_ACTION = auto()
    GET_WEATHER = auto()
    LIGHT_CONTROL = auto()
    ANSWER_QUESTION = auto()
    MUSIC_CONTROL = auto()

def run_action(
    action: Action,
    query: str,
    llm: LanguageModel,
    config: Box,
) -> str:
    """Run action."""
    match action:
        case Action.GET_WEATHER.value:
            return get_weather.main(
                query=query,
                llm=llm,
            )
        case Action.LIGHT_CONTROL.value: 
            return light_control.main(
                query=query,
                llm=llm,
                config=config,
            )
        case Action.ANSWER_QUESTION.value:
            return answer_question.main(
                query=query,
                llm=llm,
            )
        case Action.MUSIC_CONTROL.value:
            return music_control.main(
                query=query,
                llm=llm,
                config=config,
            )