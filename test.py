from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import extract
from sqlalchemy import and_
from create_schema import Base, User, Tweet, Tag
import re
import sys
import sqlalchemy

engine = create_engine('sqlite:///tweets.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

# users = [user.name for user in session.query(User).all()]

# seen_tags = {}

# for tag in session.query(Tag).all():
#   seen_tags[tag.name] = tag

tweets_ds = session.query(Tweet)
for month in [4,5,6,7]:
  tweets = session.query(Tweet).join(Tweet.tags) \
    .filter(
      and_(
        Tag.name == '#genomic',
        ~Tag.name.in_(['#23andme', '#precisionmedicine', '#personalizedmedicine', '@GenomicsEngland', '#datasharing'])
      )  
    ) \
    .filter(
      and_(
        extract('month', Tweet.timestamp) == month), 
        extract('year', Tweet.timestamp) == 2016
      )
  print tweets.count()
  #.distinct(Tweet.timestamp).all()#filter(and_(extract('month', Tweet.timestamp) == month), extract('year', Tweet.timestamp) == 2016)#.distinct(Tweet.timestamp)
# print users
# print tweets_ds.count()
# i = 0
for tweet in tweets:
  print [tag.name for tag in tweet.tags]
  break


  # tags = set([re.sub('\s','', text) for text in re.findall('([#@]\s\w+)', tweet.tweet_text)])
  # print tags
  # for tag in tags:
  #   # print tag
  #   if tag in seen_tags.keys():
  #   #   # print 'seen: ' + tag
  #     nt = seen_tags[tag]
  #     tweet.tags.append(nt)
  #     if i % 100 == 0:
  #       session.flush()
  #       session.commit()
  #   #   try:
  #   #     tweet.tags.append(nt)
  #   #   except sqlalchemy.exc.IntegrityError as err:
  #   #     print err
  #   #     session.rollback()
  #   #   except sqlalchemy.exc.InvalidRequestError as err:
  #   #     print err
  #   #     session.rollback()
  #   else:
  #     nt = Tag(name=tag)
  #     seen_tags[tag]= nt
  #     try:
  #       tweet.tags.append(nt)
  #       # session.add(nt)
  #       session.flush()
  #       session.commit()
  #     except sqlalchemy.exc.IntegrityError as err:
  #       print err
  #       session.rollback()
  #     except sqlalchemy.exc.InvalidRequestError as err:
  #       print err
  #       session.rollback()
  # #   if tag in seen_tags:

  # #   else:
  # #     nt = Tag(name=tag)
  # #     tweet.tags.append(nt)
  # #     seen_tags.append[()]
  # # print tweet.tags
  # # print tweet.timestamp.date()
  # i += 1
# print tweets_ds.count()
