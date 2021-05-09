
from sqlalchemy import create_engine, Table, Column, Integer, DateTime, MetaData, sessionmaker

meta = MetaData()


reading_names = Table(
    'reading_names',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', Integer),
)

reading_values_integer = Table(
    'reading_values_integer',
    meta,
    Column('id', Integer, primary_key=True),
    Column('reading_name_id', Integer),
    Column('value', Integer),
    Column('timestamp', DateTime),
)

reading_values_power = Table(
    'reading_values_power',
    meta,
    Column('id', Integer, primary_key=True),
    Column('reading_name_id', Integer),
    Column('voltage_value', Integer),
    Column('timestamp', DateTime),
)    

class reading_manager:
    def __init__(self):
        self.engine = create_engine('sqlite://')
        self.conn = self.engine.connect()
        Session = sessionmaker(bind = self.engine)
        self.session

    def _create_or_get_reading_name_id(self, reading_name):
        """Return a reading name ID for the requested reading_name.
        
        Will create a new reading name if necessary.
        """
#         result = self.conn.query(Customers).filter(reading_names.name == reading_name)
        result = self.conn.execute(reading_names.select().where(reading_names.c.name == reading_name)).first()
        if result:
            return result.id
        s
        return result
        for r in result:
            print(r)



if __name__ == '__main__':
    rm = reading_manager()
    print('reading ID: {}'.format(rm._create_or_get_reading_name_id('lab_power_1.voltage')))
    print('reading ID: {}'.format(rm._create_or_get_reading_name_id('lab_power_1.voltaxge')))
