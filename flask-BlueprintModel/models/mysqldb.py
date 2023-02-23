import peewee as pw

#CONEXÃO COM O BANCO DE DADOS DO MYSQL
db = pw.MySQLDatabase('dbXXXX', host = 'xx.xx.xx.xx', port = 3306, user = 'aaaaaa', passwd = 'aaaaaaaaaaaa')



class BaseModel(pw.Model):
    class Meta:
        database = db     

class tbName(BaseModel):
    id =                    pw.PrimaryKeyField()
    column1 =               pw.DateTimeField()
    column2 =               pw.TextField()
    column3 =               pw.TextField()
    column4 =               pw.TextField()
    column5 =               pw.BooleanField()



db.connect()

db.create_tables(
    [
        tbName,
    ]
)

db.close()



