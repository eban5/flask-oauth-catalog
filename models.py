from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item

engine = create_engine('sqlite:///categoryapp.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


category1 = Category(name="Soccer")
session.add(category1)
session.commit()

category2 = Category(name="Basketball")
session.add(category2)
session.commit()

category3 = Category(name="Baseball")
session.add(category3)
session.commit()

category4 = Category(name="Frisbee")
session.add(category4)
session.commit()

category5 = Category(name="Snowboarding")
session.add(category5)
session.commit()

category6 = Category(name="Rock Climbing")
session.add(category6)
session.commit()

category7 = Category(name="Foosball")
session.add(category7)
session.commit()

category8 = Category(name="Skating")
session.add(category8)
session.commit()

category9 = Category(name="Hockey")
session.add(category9)
session.commit()

item1 = Item(name="Stick", description="Interdum odio dignissim in nisi metus\
             , a elit sit dis cubilia, fringilla praesent pulvinar porta.\
             Sodales hac bibendum tincidunt risus mus himenaeos erat ac, \
             mollis semper integer tempor lacus turpis libero, ridiculus \
             primis curae aliquet nec rhoncus ante.", category=category9)
session.add(item1)
session.commit()

item2 = Item(name="Goggles",
             description="Primis dignissim mattis erat bibendum eu arcu quis\
              cursus", category=category5)
session.add(item2)
session.commit()

item3 = Item(name="Snowboard",
             description="Curae feugiat netus auctor lacus",
             category=category5)
session.add(item3)
session.commit()

item4 = Item(name="Soccer Item 1", description="Nec odio consectetur cum \
             consequat quam massa habitant placerat, nam tincidunt mi egestas \
             eu taciti velit dictum aenean, vestibulum inceptos semper \
             penatibus proin fringilla quisque. Cursus ridiculus facilisis \
             class erat varius cum consequat, ac at justo mattis magna dui \
             suscipit interdum, faucibus auctor rhoncus diam parturient a.",
             category=category1)
session.add(item4)
session.commit()

item5 = Item(name="Soccer Item 2", description="Fermentum scelerisque \
             facilisis tortor rhoncus magna maecenas, blandit ligula metus \
             amet congue fames pulvinar, eget aliquam augue eros per. Vel \
             etiam dolor ornare aliquet posuere inceptos maecenas nam, varius \
             eget ad imperdiet mi phasellus turpis nisl libero, urna \
             tristique aptent ultricies taciti montes parturient.",
             category=category1)
session.add(item5)
session.commit()

item6 = Item(name="Soccer Item 3", description="Placerat primis taciti etiam \
             ut convallis accumsan lorem tortor sapien faucibus cursus, quam \
             nulla tempor morbi rhoncus suscipit sociis in litora amet enim, \
             praesent aptent bibendum integer ornare dapibus justo rutrum \
             aliquet vivamus. Taciti dignissim neque euismod elit maecenas \
             aptent interdum mollis vel sociosqu donec, nunc gravida eget ad \
             quisque viverra vitae amet hendrerit.", category=category1)
session.add(item6)
session.commit()

item7 = Item(name="Soccer Item 4", description="Litora turpis et dignissim \
             nascetur faucibus taciti vivamus interdum, tempor dapibus lorem \
             venenatis enim conubia lacus netus hac, dis magnis vel nulla \
             phasellus bibendum fringilla. Sed torquent taciti accumsan elit \
             sagittis nulla magnis, sit praesent volutpat nam consectetur \
             velit, magna sociis id ultrices diam non.", category=category1)
session.add(item7)
session.commit()

item8 = Item(name="Frisbee", description="Interdum odio dignissim in nisi \
             metus, a elit sit dis cubilia, fringilla praesent pulvinar \
             porta. Sodales hac bibendum tincidunt risus mus himenaeos erat \
             ac, mollis semper integer tempor lacus turpis libero, ridiculus \
             primis curae aliquet nec rhoncus ante.", category=category4)
session.add(item8)
session.commit()

item9 = Item(
    name="Bat", description="Primis dignissim mattis erat bibendum eu arcu \
    quis cursus", category=category3)
session.add(item9)
session.commit()


print "Added Categories and Items."
