from django.db import models

# Create your models here.
class Voter(models.Model):
    voter_id = models.CharField(max_length=10, unique=True)
    user_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.TextField()
    is_voted=models.BooleanField()

    def __str__(self):
        return f"{self.voter_id} {self.user_name}"
    

class Ballot(models.Model):
    party_title = models.CharField(max_length=100)
    leader_name = models.CharField(max_length=100)
    total_votes=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.party_title}  {self.leader_name}"