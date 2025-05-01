from app.database.database_functions import execute, fetch_all_data, fetch_one_row_data


async def get_user(user_id: int | str) -> list | bool:
    """Get user data from Data Base."""
    query = f"""
    SELECT * 
    FROM `user`
    WHERE id = '{user_id}'
    """  # noqa: S608

    user: list | bool = await fetch_one_row_data(query)

    return user


async def add_user_to_db(
    user_id: int | str, username: str, fullname: str, lang: str
) -> None:
    """Add new user to Data Base."""
    user_ids = await get_all_user_ids() or []

    if user_id in user_ids:
        return

    query = f"""
    INSERT INTO `user` (
        id, username, fullname, lang
    )
    VALUES (
        '{user_id}', '{username}', '{fullname}', '{lang}'
    )
    """  # noqa: S608

    await execute(query)


async def update_user_data(
    user_id: int | str, column: str, new_data: int | str
) -> None:
    """Update user data in Data Base."""
    if column == "banned":
        new_data = bool(new_data)

    if isinstance(new_data, str):
        query = f"""
        UPDATE `user`
        SET {column} = '{new_data}'
        WHERE id = '{user_id}'
        """  # noqa: S608

    else:
        query = f"""
        UPDATE `user`
        SET {column} = {new_data}
        WHERE id = '{user_id}'
        """  # noqa: S608

    await execute(query)


async def get_all_users() -> list[list] | list | bool:
    """Get all users data in Data Base."""
    query = """
    SELECT *
    FROM `user`
    """

    users: list[list] | list | bool = await fetch_all_data(query)

    return users


async def get_all_user_ids() -> list[int] | list:
    """Get all user_ids in Data Base."""
    query = """
    SELECT id
    FROM `user`
    """

    user_ids = await fetch_all_data(query)

    if user_ids:
        user_ids = [int(user_list[0]) for user_list in user_ids]

    return user_ids


async def check_user_in_db(user_id: int | str) -> bool:
    """Check user in Data Base."""
    user_id = int(user_id)
    check = await get_user(user_id)

    return bool(check)


async def get_lang_from_db(user_id: int | str) -> str:
    """Get user's lang from db."""
    user = await get_user(user_id)

    return user['lang']