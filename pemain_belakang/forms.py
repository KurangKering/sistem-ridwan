from django import forms

class DataLatihBelakangForm(forms.Form):
	nama = forms.CharField()
	usia = forms.IntegerField()
	pemain_inti = forms.IntegerField()
	cadangan_main = forms.IntegerField()
	mop = forms.IntegerField()
	kk = forms.IntegerField()
	km = forms.IntegerField()
	gol = forms.IntegerField()
	kemasukan = forms.IntegerField()
	penyelamatan = forms.IntegerField()
