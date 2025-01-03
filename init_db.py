import sqlite3 as sql

def init_db():
  with sql.connect(db) as conn:
    _cur = conn.cursor()
    
    try:
      _cur.execute(create_table)
      _cur.close()
      conn.commit()
      print('TABLE CREATED WITH SUCESS')
      
    except sql.Error as e:
      print(f'Erro as criar a table depoimentos no DB: {e}')
