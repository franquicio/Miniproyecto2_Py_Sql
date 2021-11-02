import mysql.connector as db


class DB:

    def __init__(self, **config):
        self.connection = None
        self.connection = db.connect(
            host= config["host"], 
            user= config["user"], 
            passwd= config["passwd"], 
            database= config["database"]
        )
        
    def query(self, sql, args):
        cursor = self.connection.cursor()
        cursor.execute(sql, args)
        return cursor

    def insertmany(self, sql, args):
        cursor = self.connection.cursor()
        cursor.executemany(sql, args)
        rowcount = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return rowcount
    
    def insert(self, sql, args):
        cursor = self.query(sql, args)
        id = cursor.lastrowid
        self.connection.commit()
        cursor.close()
        return id
    
    def delete(self, sql, args):
        cursor = self.query(sql, args)
        self.connection.commit()
        cursor.close()

    def update(self,sql,args):
        cursor = self.query(sql, args)
        rowcount = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return rowcount    
    
    def fetch(self, sql, args):
        rows = []
        cursor = self.query(sql, args)
        if cursor.with_rows:
            rows = cursor.fetchall()
        cursor.close()
        return rows
  
    def __del__(self):
        if self.connection != None:
            self.connection.close()
    
    def __str__(self):
        return f"DB Connect {self.connection}"
