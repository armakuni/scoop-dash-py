from sqlmodel import Session, select

from src.models.internal.greeting_incidenct import GreetingIncident


class GreetingRepo:
    _session: Session

    def __init__(self, session: Session) -> None:
        self._session = session

    def count(self) -> int:
        statement = select(GreetingIncident)
        return len(self._session.exec(statement).all())

    def increment(self) -> None:
        self._session.add(GreetingIncident())
        self._session.commit()
