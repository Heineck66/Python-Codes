from twilio.rest import Client


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.account_id = "[ACC_ID]"
        self.auth_token = "[AUTH_TOKEN]"
        self.client = Client(self.account_id, self.auth_token)
        self.from_ = ("[FROM_PHONE_NUMBER]",)
        self.to = "[TO_PHONE_NUMBER]"

    def send_sms(self, message_body: str):

        message = self.client.messages.create(body=message_body, from_=self.from_, to=self.to)

        print("\n\n", message.status)
        print(message.price)
        print(message.body)
