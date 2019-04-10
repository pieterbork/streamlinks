import pafy

from . import db

class Video(db.Model):
    __tablename__ = "videos"

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String)
    title = db.Column(db.String)
    url = db.Column(db.String)
    thumb = db.Column(db.String)

    def __init__(self, link):
        p = pafy.new(link)
        best = p.getbest()
        
        self.link = link
        self.title = p.title
        self.thumb = p.thumb
        self.url = best.url

    def __repr__(self):
        return "<Video(id='{}', title='{}', url='{}', thumb='{}')>"\
                .format(self.id, self.title, self.url, self.thumb)
