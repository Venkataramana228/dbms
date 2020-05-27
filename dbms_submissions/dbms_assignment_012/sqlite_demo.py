import sqlite3
from student import Student
def get(self):
    import sqlite3
    connection = sqlite3.connect("students.db")
    crsr=connection.cursor() 
    crsr.execute('''select * from student''') 
    ans=crsr.fetchall()  
    connection.close() 
    return ans


