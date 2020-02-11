from django.db import models

class QueryType (models.Model):
    type = models.CharField(max_length=20)

    def __str__(self):
        return  self.type

class Filters (models.Model):
    query_type = models.ForeignKey(QueryType, on_delete=models.CASCADE)
    filter = models.CharField(max_length=50)
    query = models.CharField(max_length=500)
    plan = models.CharField(max_length=50)

    def __str__(self):
        return  "Query type: "+self.query_type.type+" | Query:"+self.query