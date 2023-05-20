import datetime
import mysql.connector as mc
class Reminder:

    def __init__(self, lembrete, dono, data):
        self.lembrete = lembrete
        self.dono = dono
        self.data = data

    def get_lembrete(self):
        return self.lembrete

    def get_dono(self):
        return self.lembrete

    def get_data(self):
        return self.lembrete

    def save_reminder(self):
        connection = mc.connect(host='ninadb-1.cwoklfo1flby.us-east-1.rds.amazonaws.com', user='ninaadmin505617', password='Phillipe505617', database='ninadbreminders')
        cursor = connection.cursor()
        sql = "INSERT INTO reminders (lembrete, dono, data) VALUES (%s, %s, %s)"
        values = (self.lembrete, self.dono, self.data)
        cursor.execute(sql, values)

        connection.commit()

        print(cursor.rowcount, "Lembrete Adicionado.")

def create_new_reminder(lembrete, dono):
    reminder = Reminder(lembrete, dono, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    reminder.save_reminder()
    return reminder

r1 = create_new_reminder("Fazer café para a Jade", "Emanuel Phillipe")

#create_new_reminder("Call Jeff", "Emanuel")

#ninadbreminders

#connection = mc.connect(host='ninadb-1.cwoklfo1flby.us-east-1.rds.amazonaws.com', user='ninaadmin505617', password='Phillipe505617')
#cursor = connection.cursor()
#cursor.execute('''USE ninadbreminders;''')
#cursor.execute('CREATE TABLE reminders (id INT AUTO_INCREMENT PRIMARY KEY, lembrete TINYTEXT, dono TINYTEXT, data DATE)')
