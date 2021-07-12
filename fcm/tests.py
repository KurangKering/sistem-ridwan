from django.test import TestCase, Client
from .models import DataLatihKiper
from pprint import pprint
# Create your tests here.
# 
# 

class DataTablesTestCase(TestCase):
	def test_datatables_data_latih_kiper(self):
		c = Client()
		response = c.get('/data-latih-kiper/show_all')
		print(response.content)

class PengujianTestCase(TestCase):
	def test_proses_pengujian_kiper(self):
		c = Client()
		response = c.post('/pengujian/proses_pengujian_kiper', {'jumlah_cluster': 4, 'max_iter': 1000
			, 'max_error': 0.00005})
		pprint(response.content)

		pass

class ImportTestCase(TestCase):
	def test_import_data(self):
		c = Client()
		response = None
		with open('C:/Users/Ya/Downloads/data-pemain-kiper.xlsx', 'rb') as fp:
			response = c.post('/data-latih-kiper/import', {'excel_file' : fp})
			print(response)


class ViewTestCase(TestCase):

	def setUp(self):
		self.c = Client()
		post_data = {
			'nama' : '1',
			'usia' : '1',
			'pemain_inti' : '1',
			'cadangan_main' : '1',
			'mop' : '1',
			'kk' : '1',
			'km' : '1',
			'gol' : '1',
			'kemasukan' : '1',
			'penyelamatan' : '1',
			'posisi' : '1',
		}
		data_latih = DataLatihKiper(**post_data)
		data_latih.save()

	def test_insert_data_latih(self):
		post_data = {
			'nama' : '1',
			'usia' : '1',
			'pemain_inti' : '1',
			'cadangan_main' : '1',
			'mop' : '1',
			'kk' : '1',
			'km' : '1',
			'gol' : '1',
			'kemasukan' : '1',
			'penyelamatan' : '1',
			'posisi' : '1',
		}
		response = self.c.post('/data-latih-kiper/insert', post_data)


	def test_show_all_data_latih(self):
		response = self.c.get('/data-latih-kiper/show_all')

	def test_index_data_latih(self):
		response = self.c.get('/data-latih-kiper/')


	def test_update_data_latih(self):
		post_data = {
			'id': '1',
			'nama' : '1',
			'usia' : '33',
			'pemain_inti' : '1',
			'cadangan_main' : '1',
			'mop' : '1',
			'kk' : '1',
			'km' : '1',
			'gol' : '1',
			'kemasukan' : '1',
			'penyelamatan' : '1',
			'posisi' : '1',
		}
		response = self.c.post('/data-latih-kiper/update', post_data)

	def test_detail_data_latih(self):
		post_data =	 {
			'id': '1'
		}
		response = self.c.post('/data-latih-kiper/detail', post_data)


	def test_delete_data_latih(self):
		post_data = {
			'id' : '1'
		}

		response = self.c.post('/data-latih-kiper/delete', post_data)
