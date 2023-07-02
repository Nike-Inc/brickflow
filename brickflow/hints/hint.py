from typing import Callable


# propagate type hints for decorated functions
def propagate_hint(decorator: Callable) -> Callable:
    return decorator
