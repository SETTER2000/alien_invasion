class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1905
        self.screen_height = 1040
        self.bg_color = (230, 230, 230)

        # Настройка коробля
        self.ship_speed = 1.5
