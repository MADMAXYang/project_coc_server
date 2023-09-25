from plugins.database.get_collections.chat_channels.message_pool import chat_channels_message_serial_number


def get_chat_channels_message_serial_number(chat_channel_id: int) -> int:
    result: dict = chat_channels_message_serial_number.find_one({"channel_id": str(chat_channel_id)})
    return result["channel_serial_number"]
