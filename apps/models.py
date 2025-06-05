# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Summarybets(db.Model):

    __tablename__ = 'Summarybets'

    id = db.Column(db.Integer, primary_key=True)

    #__Summarybets_FIELDS__
    userid = db.Column(db.String(255),  nullable=True)
    totalbet = db.Column(db.Boolean, nullable=True)
    totalloss = db.Column(db.Integer, nullable=True)
    totalpayout = db.Column(db.Integer, nullable=True)
    start_date = db.Column(db.String(255),  nullable=True)
    end_date = db.Column(db.String(255),  nullable=True)
    env = db.Column(db.String(255),  nullable=True)
    clientid = db.Column(db.String(255),  nullable=True)

    #__Summarybets_FIELDS__END

    def __init__(self, **kwargs):
        super(Summarybets, self).__init__(**kwargs)


class Verifytransactionssummary(db.Model):

    __tablename__ = 'Verifytransactionssummary'

    id = db.Column(db.Integer, primary_key=True)

    #__Verifytransactionssummary_FIELDS__
    totalbet = db.Column(db.Integer, nullable=True)
    totalloss = db.Column(db.Integer, nullable=True)
    totalpayout = db.Column(db.Integer, nullable=True)
    betcount = db.Column(db.Integer, nullable=True)
    gamecount = db.Column(db.Integer, nullable=True)
    currency = db.Column(db.String(255),  nullable=True)
    env = db.Column(db.String(255),  nullable=True)
    clientid = db.Column(db.String(255),  nullable=True)
    start_date = db.Column(db.String(255),  nullable=True)
    end_date = db.Column(db.String(255),  nullable=True)

    #__Verifytransactionssummary_FIELDS__END

    def __init__(self, **kwargs):
        super(Verifytransactionssummary, self).__init__(**kwargs)


class Replaytransfer(db.Model):

    __tablename__ = 'Replaytransfer'

    id = db.Column(db.Integer, primary_key=True)

    #__Replaytransfer_FIELDS__
    gameid = db.Column(db.String(255),  nullable=True)
    gameuid = db.Column(db.String(255),  nullable=True)
    gamereferencecode = db.Column(db.String(255),  nullable=True)
    gametype = db.Column(db.String(255),  nullable=True)
    gameresulttype = db.Column(db.String(255),  nullable=True)
    startdate = db.Column(db.Integer, nullable=True)
    enddate = db.Column(db.Integer, nullable=True)
    gameplay = db.Column(db.String(255),  nullable=True)
    game_results = db.Column(db.String(255),  nullable=True)
    tileid = db.Column(db.String(255),  nullable=True)
    playerid = db.Column(db.String(255),  nullable=True)
    clientplayerid = db.Column(db.String(255),  nullable=True)
    playername = db.Column(db.String(255),  nullable=True)
    currency = db.Column(db.String(255),  nullable=True)
    txid = db.Column(db.String(255),  nullable=True)
    betid = db.Column(db.String(255),  nullable=True)
    betamount = db.Column(db.Integer, nullable=True)
    payoffamount = db.Column(db.Integer, nullable=True)
    theoreticalwin = db.Column(db.Integer, nullable=True)
    playerbetstatus = db.Column(db.String(255),  nullable=True)
    resulttype = db.Column(db.String(255),  nullable=True)
    seatid = db.Column(db.Integer, nullable=True)
    bettype = db.Column(db.String(255),  nullable=True)
    handid = db.Column(db.Integer, nullable=True)
    replayurl = db.Column(db.String(255),  nullable=True)
    orderlinkurl = db.Column(db.String(255),  nullable=True)
    bankerhandtotals = db.Column(db.String(255),  nullable=True)
    playerhandtotals = db.Column(db.String(255),  nullable=True)
    rejectioncode = db.Column(db.String(255),  nullable=True)
    dealername = db.Column(db.String(255),  nullable=True)
    start_date = db.Column(db.String(255),  nullable=True)
    end_date = db.Column(db.String(255),  nullable=True)
    env = db.Column(db.String(255),  nullable=True)
    clientid = db.Column(db.String(255),  nullable=True)

    #__Replaytransfer_FIELDS__END

    def __init__(self, **kwargs):
        super(Replaytransfer, self).__init__(**kwargs)



#__MODELS__END
