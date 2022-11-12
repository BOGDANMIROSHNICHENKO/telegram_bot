import sqlite3

class SQLighter:

  def __init__(self, database_file):
    """Подключаемся к БД и сохраняем кусор соединения"""
    self.connection = sqlite3.connect(database_file)
    self.cursor = self.connection.cursor()

  def get_orders(self, id):
    """Получаем заказы"""
    with self.connection:
         return self.cursor.execute("SELECT `desc` FROM `orders` WHERE  ` user_id` = ?", (id,)).fetchall()
 
  def add_order(self, user_id, desc):
              with self.connection:
                return self.cursor.execute("INSERT INTO `orders` (`user_id`, `desc`) VALUES (?,?)", (user_id, desc))
 
 
 
 

  def close(self):
    self.cursor.close()                