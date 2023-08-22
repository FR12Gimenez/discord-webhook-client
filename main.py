import requests

def send_message(webhook_url, message):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print("Message sent")
    else:
        print("Did not send message or banned")

def main():
    webhook_url = input("Enter the webhook URL: ")
    
    while True:
        user_input = input("Enter a message: ")
        
        if user_input.lower() == "exit":
            break
        
        send_message(webhook_url, user_input)

if __name__ == "__main__":
    main()
