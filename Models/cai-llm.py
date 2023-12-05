from characterai import PyCAI

client = PyCAI('[user-token]')

char = '[character-token]'

chat = client.chat.get_chat(char)

participants = chat['participants']

if not participants[0]['is_human']:
    tgt = participants[0]['user']['username']
else:
    tgt = participants[1]['user']['username']

while True:
    message = input('You: ')

    data = client.chat.send_message(
        chat['external_id'], tgt, message
    )

    name = data['src_char']['participant']['name']
    text = data['replies'][0]['text']

    print(f"{name}: {text}")

# Get token: JSON.parse(localStorage.getItem('char_token')).value in console