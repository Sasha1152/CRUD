from django.db import models

# Create your models here.

class Task(models.Model):

	todo = 'todo'
	inprogress = 'inprogress'
	done = 'done'

	status_list = ((todo,'TODO'),
	               (inprogress, 'INPROGRESS'),
	               (done, 'DONE'))

	title = models.CharField(max_length=50)
	description = models.CharField(max_length=250)
	start_date = models.DateField(auto_now_add=True)
	status = models.CharField(max_length=12,
                                 choices=status_list,
                                 default=todo)

	def __str__(self):
		return self.title