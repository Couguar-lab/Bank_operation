# Настройка логгера
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


# Функция маскировки номера карты
def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты клиента"""
    logger.debug(f"Получен номер карты для маскировки: {card_number}")

    try:
        card_number_clear = "".join(filter(str.isdigit, card_number))
        if len(card_number_clear) < 16:
            logger.error(f"Недостаточная длина номера карты: {len(card_number_clear)} цифр")
            raise ValueError("Номер карты должен содержать не менее 16 цифр")

        masked_card = f"{card_number_clear[0:4]} {card_number_clear[4:6]}** **** {card_number_clear[-4:]}"
        logger.info(f"Номер карты успешно замаскирован: {masked_card}")
        return masked_card

    except Exception as e:
        logger.error(f"Ошибка при маскировке номера карты: {str(e)}")
        raise


# Функция маскировки номера счета
def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер счёта клиента"""
    logger.debug(f"Получен номер счёта для маскировки: {account_number}")

    try:
        account_number_clear = "".join(filter(str.isdigit, account_number))
        if len(account_number_clear) < 4:
            logger.error(f"Недостаточная длина номера счёта: {len(account_number_clear)} цифр")
            raise ValueError("Номер счёта должен содержать не менее 4 цифр")

        masked_account = f"**{account_number_clear[-4:]}"
        logger.info(f"Номер счёта успешно замаскирован: {masked_account}")
        return masked_account

    except Exception as e:
        logger.error(f"Ошибка при маскировке номера счёта: {str(e)}")
        raise
