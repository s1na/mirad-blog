from pelican import signals
import datetime
import khayyam
def miladiToShamsi(year,month,day,hour,minute,second):
	#temp=datetime(year,month,day,hour,minute,second,0).astimezone(utc)
	now = datetime.datetime(year,month,day,hour,minute,second,0)
	jalali_now = khayyam.JalaliDatetime.from_datetime(now)
	return jalali_now.strftime("%C")

def jalali(article_generator):
	for article in article_generator.dates:
		article.locale_date = miladiToShamsi(day=article.date.day,month=article.date.month,year=article.date.year,hour=article.date.hour,minute=article.date.minute,second=article.date.second)
		

def register():
	signals.article_generator_finalized.connect(jalali)
