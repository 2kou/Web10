async def check_license(event, client):
    user_id = str(event.sender_id)
    await event.respond("Veuillez entrer votre licence :")
    response = await client.wait_for(events.NewMessage(from_users=user_id))
    license_code = response.raw_text.strip()

    if license_code.startswith(user_id) and len(license_code) > 20:
        await event.respond("Licence validée ✅\nAccès débloqué.")
    else:
        await event.respond("❌ Licence invalide ou volée.")