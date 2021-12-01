from PyQt5.QtSql import QSqlTableModel


class Artist():

    def __init__(self):
        pass



    @classmethod
    def all(cls):
        model=QSqlTableModel()
        model.setTable("artist")
        model.select()
        return model