from django.db import models


# Create your models here.
class Summary(models.Model):
    rname = ""
    saddress = ""
    baddress = ""
    stime = ""
    ptype = ""
    cardname = ""
    cardnum = ""

    def setrname(self, name):
        self.rname = name
