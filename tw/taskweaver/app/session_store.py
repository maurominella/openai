import abc
from typing import Dict, List, Optional

from ..session.session import Session


class SessionStore(abc.ABC):
    @abc.abstractmethod
    def get_session(self, session_id: str) -> Optional[Session]:
        pass

    @abc.abstractmethod
    def set_session(self, session_id: str, session: Session) -> None:
        pass

    @abc.abstractmethod
    def remove_session(self, session_id: str) -> None:
        pass

    @abc.abstractmethod
    def has_session(self, session_id: str) -> bool:
        pass

    @abc.abstractmethod
    def list_all_session_ids(self) -> List[str]:
        pass


class InMemorySessionStore(SessionStore):
    def __init__(self) -> None:
        self.sessions: Dict[str, Session] = {}

    def get_session(self, session_id: str) -> Optional[Session]:
        return self.sessions.get(session_id)

    def set_session(self, session_id: str, session: Session) -> None:
        self.sessions[session_id] = session

    def remove_session(self, session_id: str) -> None:
        self.sessions.pop(session_id)

    def has_session(self, session_id: str) -> bool:
        return session_id in self.sessions

    def list_all_session_ids(self) -> List[str]:
        return list(self.sessions.keys())
