from django.forms import ModelForm
from .models import Instruction

class InstructionForm(ModelForm):
  class Meta:
    model = Instruction
    fields = ['step_no', 'description']