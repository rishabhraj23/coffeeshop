import json
import requests

# Define a function to send email using the API Gateway and Lambda
def send_email_notification(recipient_email, order_status, order_id):
    try:
        # Replace with your actual API Gateway endpoint
        API_URL = "https://ay4wp7fc97.execute-api.us-west-1.amazonaws.com/prod/send_emails"
        API_KEY = "rKTmbOUNfR6Wkv5MM3ALV7cmYKpADL3J9zdlPwcS"

        # Prepare the payload for the API request
        payload = {
            "recipient_email": recipient_email,
            "order_status": order_status,
            "order_id": str(order_id)  # Ensure order_id is passed as a string
        }

        # Set the request headers, including the API key for authentication
        headers = {
            "Content-Type": "application/json",
            "x-api-key": API_KEY
        }

        # Send POST request to API Gateway
        response = requests.post(API_URL, data=json.dumps(payload), headers=headers)

        # Check the response from API Gateway
        if response.status_code == 200:
            return {"status": "success", "message": "Email sent successfully."}
        else:
            return {"status": "error", "message": f"Failed to send email. API Response: {response.text}"}

    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": f"Error sending email: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": f"An unexpected error occurred: {str(e)}"}
