from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .forms import DataLatihKiperForm
from .models import DataLatihKiper
from utils.helper import *
from django.forms.models import model_to_dict
import openpyxl
from itertools import islice
from libraries.factories import FCMFactory
import numpy as np
import copy
from django.db import connection


def data_latih_index(request):
	"""
	{ function_description }

	:param      request:  The request
	:type       request:  { type_description }

	:returns:   { description_of_the_return_value }
	:rtype:     { return_type_description }
	"""
	return render(request, 'kiper/data-latih/index.html')



@csrf_exempt
def data_latih_detail(request):
    id_data_latih_kiper = request.POST.get('id')
    if (id_data_latih_kiper == None or id_data_latih_kiper == ''):
    	context = context_response(False, 'id tidak boleh kosong')


    data_latih_kiper = DataLatihKiper.objects.get(pk=id_data_latih_kiper)
    serial = model_to_dict(data_latih_kiper)

    context = context_response(True, serial)

    return JsonResponse(context, safe=False)


@csrf_exempt
def data_latih_create_or_update(request):

	id_data_latih = request.POST.get('id')

	if (id_data_latih == '' or id_data_latih == None):
		context = data_latih_insert(request)
	else:
		context = data_latih_update(request)

	return JsonResponse(context, safe=False)


@csrf_exempt
def data_latih_insert(request):

	form = DataLatihKiperForm(request.POST)
	if form.is_valid():
		post_data = form.cleaned_data
		data_latih_kiper = DataLatihKiper()
		data_latih_kiper.nama = post_data['nama']
		data_latih_kiper.usia = post_data['usia']
		data_latih_kiper.pemain_inti = post_data['pemain_inti']
		data_latih_kiper.cadangan_main = post_data['cadangan_main']
		data_latih_kiper.mop = post_data['mop']
		data_latih_kiper.kk = post_data['kk']
		data_latih_kiper.km = post_data['km']
		data_latih_kiper.gol = post_data['gol']
		data_latih_kiper.kemasukan = post_data['kemasukan']
		data_latih_kiper.penyelamatan = post_data['penyelamatan']

		data_latih_kiper.set_bobot_data()
		data_latih_kiper.save()

		context = context_response(True, 'sukses menambah data data_latih_kiper')

	else:
		context = context_response(False, form.errors)

	return context

@csrf_exempt
def data_latih_update(request):
	form = DataLatihKiperForm(request.POST)

	if form.is_valid():
		post_data = form.cleaned_data
		data_latih_kiper = DataLatihKiper.objects.get(pk=request.POST.get('id'))
		data_latih_kiper.nama = post_data['nama']
		data_latih_kiper.usia = post_data['usia']
		data_latih_kiper.pemain_inti = post_data['pemain_inti']
		data_latih_kiper.cadangan_main = post_data['cadangan_main']
		data_latih_kiper.mop = post_data['mop']
		data_latih_kiper.kk = post_data['kk']
		data_latih_kiper.km = post_data['km']
		data_latih_kiper.gol = post_data['gol']
		data_latih_kiper.kemasukan = post_data['kemasukan']
		data_latih_kiper.penyelamatan = post_data['penyelamatan']

		data_latih_kiper.set_bobot_data()
		data_latih_kiper.save()
		context = context_response(True, ['sukses merubah data latih'])

	else:
		context = context_response(False, form.errors)

	return context

@csrf_exempt
def data_latih_delete(request):
    id_data_latih_kiper = request.POST.get('id')
    data_latih_kiper = DataLatihKiper.objects.get(pk=id_data_latih_kiper)

    if (data_latih_kiper.delete()):
    	context = context_response(True, 'sukses menghapus data latih')
    else:
    	context = context_response(False, 'gagal menghapus data latih')

    return JsonResponse(context, safe=False)


@csrf_exempt
def data_latih_import(request):

	excel_file = request.FILES['excel_file']

	wb = openpyxl.load_workbook(excel_file)
	worksheet = wb['sheet1']
	excel_data = []

	field_names = [
		'nama',
		'usia',
		'pemain_inti',
		'cadangan_main',
		'mop',
		'kk',
		'km',
		'gol',
		'kemasukan',
		'penyelamatan',
		]

	for row in islice(worksheet.iter_rows(), 1, None):

		row_data = dict()
		for index in range(len(row)):
			row_data[field_names[index]] = str(row[index].value).strip()
			data_latih_kiper = DataLatihKiper(**row_data)
			data_latih_kiper.set_bobot_data()
		excel_data.append(data_latih_kiper)



	if request.POST.get('hapus_seluruh_data') == 'on':
		DataLatihKiper.objects.all().delete()
		table_name = DataLatihKiper.objects.model._meta.db_table

		sql = ""

		if (connection.vendor == 'sqlite'):
			sql = "DELETE FROM SQLite_sequence WHERE name='{}';".format(table_name)
		elif (connection.vendor == 'postgresql'):
			sequence = f"{table_name}_id_seq"
			sql = "ALTER SEQUENCE {} RESTART WITH 1;".format(sequence)


		with connection.cursor() as cursor:
			cursor.execute(sql)
			
	DataLatihKiper.objects.bulk_create(excel_data)
	total_data = len(DataLatihKiper.objects.all().values())
	context = context_response(True, {'total_data': total_data})
	return JsonResponse(context, safe=False)

#
# fungsi-fungsi terkait pengujian FCM
#
#
def pengujian_index(request):
	"""
	{ function_description }

	:param      request:  The request
	:type       request:  { type_description }
	"""
	return render(request, 'kiper/pengujian/index.html')

@csrf_exempt
def pengujian_proses(request):
	jumlah_cluster = int(request.POST.get('jumlah_cluster'))
	max_iter = int(request.POST.get('max_iter'))
	max_error = float(request.POST.get('max_error'))

	data_latih_all_fields = DataLatihKiper.objects.all()
	data_latih = list(data_latih_all_fields.values('id', 'nama', 'norm_usia', 'norm_pemain_inti', 'norm_cadangan_main', 'norm_mop', 'norm_kk', 'norm_km', 'norm_gol', 'norm_kemasukan', 'norm_penyelamatan'))

	data_to_list = [[v for k, v in d.items() if not k in ['id', 'nama']] for d in data_latih]


	params = {
	'n_clusters': jumlah_cluster,
	'max_iter': max_iter,
	'm': 2,
	'error': max_error,
	'random_state': 42,
	}

	factory = FCMFactory()
	fcm = factory.createFCM(**params)

	numpy_data = np.array(data_to_list)
	fcm.fit(numpy_data)
	hasil_cluster = fcm.predict(numpy_data)

	data_with_hasil = copy.deepcopy(data_latih)
	for x in range(len(data_to_list)):
		data_with_hasil[x]['cluster'] = hasil_cluster[x]
		convert_to_string = {k:str(v) for k,v in data_with_hasil[x].items()}
		data_with_hasil[x] = convert_to_string

	data_latih_numpy = np.array(data_latih)	
	unique_clusters = np.unique(hasil_cluster)
	data_per_cluster = []
	indices_clusters = []
	data_latih_clusters = []
	attributes = [
			'norm_usia',
			'norm_pemain_inti',
			'norm_cadangan_main',
			'norm_mop',
			'norm_kk',
			'norm_km',
			'norm_gol',
			'norm_kemasukan',
			'norm_penyelamatan']

	averages = {f"avg_{'_'.join(j.split('_')[1:])}": [] for j in attributes}
	title_averages = [f"Grafik Rata-Rata {' '.join(j.split('_')[1:])}" for j in attributes]
	key_averages = list(averages.keys())
	for i in unique_clusters:
		indices = np.where(hasil_cluster == i)[0].tolist()
		cluster = data_latih_numpy[indices]
		for j in range(len(attributes)):
			avg = np.mean([x[attributes[j]] for x in cluster])
			averages[key_averages[j]].append(avg)


		indices_clusters.append(indices)
		data_latih_clusters.append(cluster.tolist())






	hasil_cluster_list = hasil_cluster.tolist()
	initial_u_list = fcm.initial_u.copy().tolist()
	final_u_list = fcm.u.copy().tolist()
	current_error = fcm.list_of_error[-1]

	output = {
		'jumlah_cluster': jumlah_cluster,
		'max_iter': max_iter,
		'max_error': max_error,
		'data_latih': data_latih,
		'initial_u': initial_u_list,
		'list_of_error': fcm.list_of_error,
		'hasil_cluster': hasil_cluster_list,
		'current_error': current_error,
		'final_u': final_u_list,
		'data_latih_clusters': data_latih_clusters,
		'averages': averages,
		'title_averages': title_averages,

	}

	context = context_response(True, output)
	return JsonResponse(context, safe=False)



