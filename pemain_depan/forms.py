from django import forms

class DataLatihPemainDepanForm(forms.Form):
	nama = forms.CharField()
	usia = forms.IntegerField()
	pemain_inti = forms.IntegerField()
	cadangan_main = forms.IntegerField()
	mop = forms.IntegerField()
	kk = forms.IntegerField()
	km = forms.IntegerField()
	gol = forms.IntegerField()
	assist = forms.IntegerField()
	pelanggaran = forms.IntegerField()
	dilanggar_lawan = forms.IntegerField()
	akurasi_tembakan = forms.IntegerField()
	akurasi_operan = forms.IntegerField()
	akurasi_umpan_silang = forms.IntegerField()
	sukses_dribel = forms.IntegerField()
