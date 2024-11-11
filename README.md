## Elitely Telegram Bot (Python)

This **Telegram bot for Elitely** uses **Python**, **Flask**, and an **ngrok server**. The ngrok server can be replaced using a backend server.

The current bot used in the `config.py` file is called **Testbot**.

You can find this bot using: [t.me/stuntaz_bot](https://t.me/stuntaz_bot)

### Important Notes:

- Please note that if you are using your **own backend server** for testing instead of ngrok, ensure you are **port forwarding** the URL for your backend server to the port opened in the `app.py` file. The current port is set to **8000**. Also, replace the `NGROK_URL` in the `config.py` file with the **backend server HTTPS URL**. You are also free to change the name for the variable in `config.py` from `NGROK_URL` to whatever name you see fit. If you choose to use an **ngrok server** with Testbot, please ensure to update the `NGROK_URL` in `config.py` to your **unique forwarding URL created by ngrok**.

- The current iteration of the **POST /webhook** API call checks whether a user has a registered number by verifying if the `USER_PHONE_NUMBER` object variable in the `elitely_number_verification.py` file is empty. In future iterations, a solution could be to cross-check a **backend database** to see if a number is registered for that user. A simple function can be created to check and retrieve the value.

- **Hyperlinks** have yet to be embedded in the bot responses. This can be resolved once the appropriate links are provided.

After initializing the bot and sending `/start`, the **chat_id** can be retrieved and saved to a database for future use in API calls. You can temporarily test the API calls `GET /LurkerRequest/<string:chat_id>` and `GET /InfluencerPayment/<string:chat_id>` by obtaining the **chat_id** as follows:

1. Open this URL in your web browser or Postman: `https://api.telegram.org/bot<BOT_TOKEN>/getUpdates`.
   - Replace `<BOT_TOKEN>` with your bot's token.
   - Locate the **id** value within the `chat` JSON object; this is the `chat_id` you'll use for API testing.

2. To retrieve the `chat_id` using the **TestBot** created for this demo:
   - Go to [t.me/stuntaz_bot](https://t.me/stuntaz_bot) and send the `/start` command.
   - Once the bot is initialized, use the URL format mentioned above to fetch the `chat_id`.

### Installation

1. **Download ngrok** into the project root directory: [https://ngrok.com/download](https://ngrok.com/download)

2. Navigate to the root directory in terminal and run:
   ```bash
   ./ngrok http 8000
3. If you are using the Testbot created for this demo, then the TOKEN variable in config.py can be kept the same.

4. If you are creating your own Telegram bot, replace the TOKEN variable in config.py with your newly created token.

5. Add your ngrok HTTPS URL to the NGROK_URL variable in config.py.

6. Configure conditional actions based on Telegram message text in telegram_bot.py in the TelegramBot.action class method.

7. Run the app server (make sure Python 3.8 is in your PATH):
```bash
python3.8 app.py
```
API Paths
Initializing the Bot and Sending Greeting Message / Phone Number Verification
POST /webhook

This endpoint will start the bot when prompted using /start, provide Telegram servers with your Webhook, check for phone number registration, and retrieve the chat_id, first_name, and incoming text message.

Request Body:

Header:
Content-Type: application/json

```json
{   
    "message": {
        "chat_id": "<string:chat_id>",
        "incoming_message_text": "<string:text>",
        "first_name": "<string:first_name>"
    }
}
```
Sample Response (Success):
HTTP 200:

```json
{
    "message": {
        "success": true
    }
}
```
Sending a Lurker Request to Influencer
GET /LurkerRequest/string:chat_id

This endpoint takes the chat_id of the user to send the influencer a Lurker request notification.

Request Body:

Header:
Content-Type: application/json
```json
{
    "chat_id": "<string:chat_id>"
}

```

Sample Response (Success):
HTTP 200:

```json
{
    "message": {
        "success": true
    }
}
```

Sending an Influencer Payment Request to the Lurker
GET /InfluencerPayment/string:chat_id

This endpoint takes the chat_id of the user to send the influencer a payment request notification.

Request Body:

Header:
Content-Type: application/json
```json
{
    "chat_id": "<string:chat_id>"
}
```
Sample Response (Success):
HTTP 200:

```json
{
    "message": {
        "success": true
    }
}
```
