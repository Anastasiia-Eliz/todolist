from dataclasses import field
from typing import List

from marshmallow_dataclass import dataclass
from marshmallow import EXCLUDE


@dataclass
class MessageFrom:
	id: int
	is_bot: bool
	first_name: str
	last_name: str | None
	username: str

	class Meta:
		unknown = EXCLUDE


@dataclass
class MessageChat:
	id: int
	first_name: str | None
	username: str | None
	last_name: str | None
	type: str
	title: str | None

	class Meta:
		unknown = EXCLUDE




@dataclass
class Message:
	message_id: int
	msg_from: MessageFrom = field(metadata={'data_key': 'from'})
	chat: MessageChat
	date: int
	text: str


	class Meta:
		unknown = EXCLUDE


@dataclass
class UpdateOdj:
	update_id: int
	message: Message

	class Meta:
		unknown = EXCLUDE


@dataclass
class GetUpdatesResponse:
	ok: bool
	result: List[UpdateOdj]

	class Meta:
		unknown = EXCLUDE


@dataclass
class SendMessageResponse:
	ok: bool
	result: Message

	class Meta:
		unknown = EXCLUDE
