import sqlite3
import os
import csv

def main():

  
   
    db_path = 'DATABASE FILE PATH'
    csv_path = 'CSV FILE PATH'

    
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    
   
    csv_file = open(csv_path, 'w')

    
    csv_writer = csv.writer(csv_file)
    
   
    student_info = c.execute('SELECT * FROM YOUR_TABLE_HERE;').fetchall()
    
    
    print('[+] Writing Database rows to CSV file')

   
    for i in student_info:
        csv_writer.writerow(i)


   
    print('[+] FINISHED! CSV file is now ready for use.')
    
    
#Call main function
main()
