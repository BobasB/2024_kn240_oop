import logging

logging.basicConfig(filename="module.log", 
                    level=logging.WARNING, 
                    encoding='utf8',
                    format="%(filename)s:%(levelname)s::::=== %(message)s ===")

logging.warning("Логи з модуля!")
