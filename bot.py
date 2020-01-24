import telebot

bot = telebot.TeleBot('731585587:AAFoo1xgnU7wBo92Yjwt1t-AKZFadpLFKRs')


@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location', 'contact', 'pinned_message'])
def get_text_messages(message):
    if message.content_type == 'text':
        bot.send_message(message.from_user.id, message.text)

    elif message.content_type == 'audio':
        bot.send_audio(message.from_user.id, message.audio.file_id)

    elif message.content_type == 'document':
        bot.send_document(message.from_user.id, message.document.file_id)

    elif message.content_type == 'photo' and len(message.photo) > 0:
        bot.send_photo(message.from_user.id, message.photo[0].file_id)

    elif message.content_type == 'sticker':
        bot.send_sticker(message.from_user.id, message.sticker.file_id)

    elif message.content_type == 'video':
        bot.send_video(message.from_user.id, message.video.file_id)

    elif message.content_type == 'video_note':
        bot.send_video_note(message.from_user.id, message.video_note.file_id)

    elif message.content_type == 'voice':
        bot.send_voice(message.from_user.id, message.voice.file_id)

    elif message.content_type == 'location':
        bot.send_location(message.from_user.id, message.location.latitude, message.location.longitude)

    elif message.content_type == 'contact':
        bot.send_contact(message.from_user.id, message.contact.phone_number, message.contact.first_name, message.contact.last_name)


bot.polling(none_stop=True, interval=0)
