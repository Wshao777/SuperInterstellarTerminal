# How to Set Up LINE Notify and Messaging API

This guide explains how to get the necessary tokens and secrets to integrate LINE notifications and bots into the Lightning Empire system.

---

## Part 1: LINE Notify (for simple notifications)

LINE Notify is used for sending simple text or image messages to a LINE chat or group. It's perfect for alerts.

1.  **Go to the LINE Notify Website:**
    - Navigate to [https://notify-bot.line.me/my/](https://notify-bot.line.me/my/) and log in with your LINE account.

2.  **Generate a Token:**
    - Scroll down to the "Generate token" section.
    - Give your token a name (e.g., "LightningEmpireAlerts").
    - Select the chat you want to receive notifications in. You can choose "1-on-1 chat with LINE Notify" to get messages yourself, or select a group you are in.
    - Click "Generate token".

3.  **Copy Your Token:**
    - A token will be generated (e.g., `aBcDeFgHiJkLmNoPqRsTuVwXyZ1234567890`).
    - **Copy this token immediately.** This is the only time it will be shown.
    - Paste this value into the `LINE_NOTIFY_TOKEN` field in your `.env` file.

4.  **Invite the Bot (for groups):**
    - If you selected a group, you must invite the "LINE Notify" official account into that group chat.

---

## Part 2: LINE Messaging API (for interactive bots)

The Messaging API is more powerful and allows for two-way communication, rich menus, and more. The user provided a guide from a platform called "MaiAgent," which I have adapted below.

### 1. Create a Provider and Channel
- Go to the **LINE Developers Console**: [https://developers.line.biz/console/](https://developers.line.biz/console/)
- Create a **Provider** (e.g., "Lightning Empire").
- Within your provider, create a new **Channel** and select **Messaging API**.
- Fill in the required details for your channel (bot name, description, etc.).

### 2. Get Channel Credentials
- Once the channel is created, navigate to the **"Messaging API"** tab within your channel's settings.
- Here you will find:
    - **Channel ID**
    - **Channel secret**
- Scroll down to the bottom and issue a **Channel access token (long-lived)**.

### 3. Configure Webhook Settings
- In the "Messaging API" tab, enable "Use webhook".
- Set the **Webhook URL**. This will be the URL of our running backend server (e.g., `https://your-domain.com/webhook/line`).
- Ensure "Auto-reply messages" is **Disabled** and "Greeting messages" is **Disabled**. This allows our backend application to handle all messages.

### 4. Add to `.env`
- Take the credentials from step 2 and add them to your `.env` file. You may need to add new variables for these, for example:
  ```
  LINE_CHANNEL_ID=...
  LINE_CHANNEL_SECRET=...
  LINE_CHANNEL_ACCESS_TOKEN=...
  ```

Your system is now ready for LINE integration!