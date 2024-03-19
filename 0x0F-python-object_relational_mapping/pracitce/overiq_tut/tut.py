import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String,\
DateTime, ForeignKey, Numeric, CheckConstraint, func, select, update

from datetime import datetime

engine = create_engine("mysql://loayalsaid1:Loay_alsaid04@localhost/overiq_orm_tut", echo=True)
conn = engine.connect()

metadata = MetaData()


customers = Table('customers', metadata,
    Column('id', Integer(), primary_key=True),
    Column('first_name', String(100), nullable=False),
    Column('last_name', String(100), nullable=False),
    Column('username', String(50), nullable=False),
    Column('email', String(200), nullable=False),
    Column('address', String(200), nullable=False),
    Column('town', String(50), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)


items = Table('items', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(200), nullable=False),
    Column('cost_price', Numeric(10, 2), nullable=False),
    Column('selling_price', Numeric(10, 2),  nullable=False),
    Column('quantity', Integer(), nullable=False),
    CheckConstraint('quantity > 0', name='quantity_check')
)


orders = Table('orders', metadata,
    Column('id', Integer(), primary_key=True),
    Column('customer_id', ForeignKey('customers.id')),
    Column('date_placed', DateTime(), default=datetime.now),
    Column('date_shipped', DateTime())
)


order_lines = Table('order_lines', metadata,
    Column('id', Integer(), primary_key=True),
    Column('order_id', ForeignKey('orders.id')),
    Column('item_id', ForeignKey('items.id')),
    Column('quantity', Integer())
)


metadata.create_all(engine)





from sqlalchemy.exc import IntegrityError
from sqlalchemy import insert
ins = customers.insert().values(
    first_name = "John",
    last_name = 'Green',
    username = 'johngreen',
    email = 'johngreen@mail.com',
    address = '164 Hidden Valley Road',
    town = 'Norfolk'    
)

# conn.execute(ins)


conn.execute(insert(customers), [
    {
        "first_name": "John", 
        "last_name": "Lara", 
        "username": "johnlara", 
        "email":"johnlara@mail.com", 
        "address": "3073 Derek Drive",
        "town": "Norfolk"
    },
    {
            "first_name": "Sarah", 
            "last_name": "Tomlin", 
            "username": "sarahtomlin", 
            "email":"sarahtomlin@mail.com",
            "address": "3572 Poplar Avenue",
            "town": "Norfolk"
        },
        {
            "first_name": "Pablo", 
            "last_name": "Gibson", 
            "username": "pablogibson", 
            "email":"pablogibson@mail.com",
            "address": "3494 Murry Street",
            "town": "Peterbrugh"
        },
        {
            "first_name": "Pablo", 
            "last_name": "Lewis", 
            "username": "pablolewis", 
            "email":"pablolewis@mail.com",
            "address": "3282 Jerry Toth Drive",
            "town": "Peterbrugh"
        },
    ])


items_list = [
    {
        "name":"Chair",
        "cost_price": 9.21,
        "selling_price": 10.81,
        "quantity": 5
    },
    {
        "name":"Pen",
        "cost_price": 3.45,
        "selling_price": 4.51,
        "quantity": 3
    },
    {
        "name":"Headphone",
        "cost_price": 15.52,
        "selling_price": 16.81,
        "quantity": 50
    },
    {
        "name":"Travel Bag",
        "cost_price": 20.1,
        "selling_price": 24.21,
        "quantity": 50
    },
    {
        "name":"Keyboard",
        "cost_price": 20.12,
        "selling_price": 22.11,
        "quantity": 50
    },
    {
        "name":"Monitor",
        "cost_price": 200.14,
        "selling_price": 212.89,
        "quantity": 50
    },
    {
        "name":"Watch",
        "cost_price": 100.58,
        "selling_price": 104.41,
        "quantity": 50
    },
    {
        "name":"Water Bottle",
        "cost_price": 20.89,
        "selling_price": 25.00,
        "quantity": 50
    },
]

order_list = [
    {
        "customer_id": 1
    },
    {
        "customer_id": 1
    }
]

order_line_list = [
    {
        "order_id": 1,
        "item_id": 1,
        "quantity": 5
    }, 
    {
        "order_id": 1,
        "item_id": 2,
        "quantity": 2
    }, 
    {
        "order_id": 1,
        "item_id": 3,
        "quantity": 1
    },
    {
        "order_id": 2,
        "item_id": 1,
        "quantity": 5
    },
    {
        "order_id": 2,
        "item_id": 2,
        "quantity": 5
    },
]

# r = conn.execute(insert(items), items_list)
# r = conn.execute(insert(orders), order_list)
# r = conn.execute(insert(order_lines), order_line_list)

from sqlalchemy.sql import func
def dispatch_order(order_id):

    r = conn.execute(select([func.count('*')]).where(orders.c.id == order_id))
    if not r.scaler():
        raise ValueError("Invalid order id: {}".format(order_id))
    
    s = select([order_lines.c.item_id, order_lines.c.quattity]).where(
        order_lines.c.order_id == order_id)
    
    rs = conn.execute(s)
    ordered_items = rs.fetchall()


    transaction = conn.begin()

    try:
        for i in ordered_items:
            u = update(items).where(
                items.c.id == i[0]
            ).values(quantity = items.quantity - i[1])

            rs = conn.execute(u)
        
        u = update(orders).where(id=order_id).values(
            date_shipped=datetime.now()
        )
        conn.execute(u)
        print("done")
        transaction.commit()
    except IntegrityError as e:
        transaction.rollback()
        print("transation not completed")


from sqlalchemy.orm import Relationship

x = Relationship()

