def send_email (message, recipient, sender='university.help@gmail.com'):

    if "@" not in send_email or not (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net")):
        return False
    return True

 if not send_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

if sender == recipient:
    print("Нельзя отправить письмо самому себе!")
    return
  if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email("это сообщение для проверки связи", "vasyok1337@gmail.com")
send_email("вы видите это сообщение как лучший студент курса!", "urban.fan@mail.ru",
           sender='urban.info@gmail.com')
send_email("пожалуйста,исправьте задание,", "urban.student@mail.ru", sender="urban.teacher@mail.ru")
send_email("напоминаю самому себе о вебинаре", "urban.teacher@mail.ru",
           sender="urban.student@mail.ru")