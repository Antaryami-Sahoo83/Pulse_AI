from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER_OPTIONS = {
      'M': 'Male',
      'F': "Female"
}

CHEST_PAIN_OPTIONS = {
      'TA': 'Typical Angina',
      'ATA': 'Atypical Angina', 
      'NAP': 'Non-Anginal Pain', 
      'ASY': 'Asymptomatic'
}

BLOOD_SUGER_OPTIONS = {
      '0': "Less than or equal to 120",
      '1': "More than to 120"
}
RESTING_ECG_OPTIONS = {
      'Normal': 'Normal', 
      'ST': 'Having ST-T wave abnormality', 
      'LVH': "Showing probable or definite left ventricular hypertrophy by Estes' criteria"
}

EXERCISE_ANGINA_OPTIONS = {
      'Y': 'Yes',
      'N': 'No'
}

ST_SLOPE_OPTIONS = {
      'Flat': 'Flat', 
      'Up': 'Upsloping', 
      'Down': 'Downsloping'
}

class HeartVital(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      created_at = models.DateTimeField(auto_now_add=True)
      Age = models.IntegerField()
      Sex = models.CharField(max_length=255, choices=GENDER_OPTIONS)
      ChestPainType = models.CharField(max_length=255, choices=CHEST_PAIN_OPTIONS, verbose_name='Chest Pain Type')
      RestingBP = models.IntegerField(verbose_name='Resting Blood Presure (60-220)')
      Cholesterol = models.IntegerField()
      FastingBS = models.CharField(max_length=255, choices=BLOOD_SUGER_OPTIONS, verbose_name='Fasting Blood Suger (60 - 900)')
      RestingECG = models.CharField(max_length=255, choices=RESTING_ECG_OPTIONS, verbose_name='Resting ECG Condition')
      MaxHR = models.IntegerField(verbose_name='Maximum Heart Rate (60 - 220)')
      ExerciseAngina = models.CharField(max_length=255, choices=EXERCISE_ANGINA_OPTIONS, verbose_name='Exercise Angina')
      Oldpeak = models.FloatField(verbose_name='Oldpeak(-2.5 - +2.5)')
      ST_Slope = models.CharField(max_length=255, choices=ST_SLOPE_OPTIONS)
      heart_disease = models.CharField(max_length=255, blank=True)
      prediction_probability = models.CharField(max_length=255, blank=True)

      def __str__(self):
            return self.user.username








# Create your models here.
