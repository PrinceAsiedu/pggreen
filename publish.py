async def publish(pool, channel: str, messages: list):
    """
    Send a list of notifications to a PostgreSQL channel.

    Args:
        pool (aiopg.Pool): The aiopg connection pool.
        channel (str): The PostgreSQL channel to send notifications to.
        messages (list): A list of messages to send.
    """
    
    # Acquire a connection from the aiopg connection pool
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            try:
                for msg in messages:
                    print(f"Send -> {msg}")
                    # Execute the NOTIFY command on the PostgreSQL channel with the current message.
                    # This command asynchronously sends a notification to the channel.
                    await cur.execute(f"NOTIFY {channel}, %s", (msg,))
            
            except Exception as error:
                print(f"Error Occurred -> {error}")
                print("Shutting down publisher")
            
            finally:
                # This is often useful to let listeners know that no more messages will be sent.
                await cur.execute(f"NOTIFY {channel}, 'finish'")
