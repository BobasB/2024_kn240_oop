import logging

logging.basicConfig(filename="logs.log", 
                    level=logging.WARNING, 
                    encoding='utf8',
                    format="%(filename)s:%(levelname)s::::=== %(message)s ===")

logging.warning()
