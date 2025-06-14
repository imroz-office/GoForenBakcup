import requests
from django.conf import settings

def send_whatsapp_message(to_number, message_type='text', content=None, template_name=None, template_params=None, button_url_params=None ):
    if not to_number.startswith("91") and len(to_number) == 10:
        to_number = f"91{to_number}"

    url = f"https://api.wbbox.io/v3/{settings.WBBOX_PHONE_NUMBER_ID}/messages"
    headers = {
        'Content-Type': 'application/json',
        'apikey': settings.WBBOX_API_KEY,
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
    }

    if message_type == 'text':
        payload.update({
            "type": "text",
            "preview_url": False,
            "recipient_type": "individual",
            "text": {
                "body": content
            }
        })
    elif message_type == 'template':
        template_payload = {
            "name": template_name,
            "language": {
                "code": "en"
            },
            "components": []
        }

        # Add body parameters
        if template_params:
            template_payload["components"].append({
                "type": "body",
                "parameters": [
                    {"type": "text", "text": str(param)} for param in template_params
                ]
            })

        # Add button URL parameters if available
        if button_url_params:
            template_payload["components"].append({
                "type": "button",
                "sub_type": "url",
                "index": 0,  # Adjust if using multiple buttons
                "parameters": [
                    {"type": "text", "text": str(param)} for param in button_url_params
                ]
            })

        payload.update({
            "type": "template",
            "template": template_payload
        })

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print("✅ WhatsApp message sent:", response.json())
            return True
        else:
            print("❌ WhatsApp error:", response.status_code, response.text)
            return False
    except Exception as e:
        print("🚨 Exception:", str(e))
        return False



# import requests
# from django.conf import settings

# def send_whatsapp_message(to_number, message_type='text', content=None, template_name=None, template_params=None):
#     if not to_number.startswith("91") and len(to_number) == 10:
#         to_number = f"91{to_number}"

#     url = f"https://api.wbbox.io/v3/{settings.WBBOX_PHONE_NUMBER_ID}/messages"
#     headers = {
#         'Content-Type': 'application/json',
#         'apikey': settings.WBBOX_API_KEY,
#     }

#     payload = {
#         "messaging_product": "whatsapp",
#         "to": to_number,
#     }

#     if message_type == 'text':
#         payload.update({
#             "type": "text",
#             "preview_url": False,
#             "recipient_type": "individual",
#             "text": {
#                 "body": content
#             }
#         })
#     elif message_type == 'template':
#         payload.update({
#             "type": "template",
#             "template": {
#                 "name": template_name,
#                 "language": {
#                     "code": "en"
#                 },
#                 "components": [{
#                     "type": "body",
#                     "parameters": [
#                         {"type": "text", "text": param} for param in template_params
#                     ]
#                 }]
#             }
#         })

#     try:
#         response = requests.post(url, json=payload, headers=headers)
#         if response.status_code == 200:
#             print("✅ WhatsApp message sent:", response.json())
#             return True
#         else:
#             print("❌ WhatsApp error:", response.status_code, response.text)
#             return False
#     except Exception as e:
#         print("🚨 Exception:", str(e))
#         return False

