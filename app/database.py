import sqlalchemy
import databases

DATABASE_URL = "sqlite:///online_store.db"
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table("users", metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(50)),
                         sqlalchemy.Column("surname", sqlalchemy.String(50)),
                         sqlalchemy.Column("email", sqlalchemy.String(50)),
                         sqlalchemy.Column("password", sqlalchemy.String(120)),)

goods = sqlalchemy.Table("goods", metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("name", sqlalchemy.String(50)),
                         sqlalchemy.Column("description", sqlalchemy.String(200)),
                         sqlalchemy.Column("price", sqlalchemy.Float))

orders = sqlalchemy.Table("orders", metadata,
                         sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
                         sqlalchemy.Column("user_id", sqlalchemy.ForeignKey("users.id"), nullable=False),
                         sqlalchemy.Column("goods_id", sqlalchemy.ForeignKey("goods.id"), nullable=False),
                         sqlalchemy.Column("order_date", sqlalchemy.DATE),
                         sqlalchemy.Column('status', sqlalchemy.String(20)))

metadata.create_all(engine)