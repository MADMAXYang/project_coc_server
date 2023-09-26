from plugins.database.get_collections.chat_channels.message_pool import chat_channels_message_pool


def get_chat_channels_message_id(chat_channel_id: int, ) -> int:
    result: dict = chat_channels_message_pool.find_one({"channel_id": chat_channel_id})
    return result["channel_message_id"]


def update_chat_channels_message_id(chat_channel_id: int, ) -> None:

    chat_channels_message_pool.update_one(
        {
            "channel_id": chat_channel_id
        },
        {
            "$set": {
                "channel_message_id": get_chat_channels_message_id(chat_channel_id) + 1
            }
        }
    )
