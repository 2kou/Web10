async def process_payment(event, client):
    user_id = event.sender_id
    message = f"Demande de paiement de {user_id}"
    await client.send_message(int(os.getenv("ADMIN_ID")), message)
    await event.respond("Demande envoyée à l'administrateur.")