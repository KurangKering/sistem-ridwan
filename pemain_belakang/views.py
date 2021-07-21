from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .forms import DataLatihBelakangForm
from fcm.models import DataLatihPemain
from utils.helper import *
from django.forms.models import model_to_dict
import openpyxl
from itertools import islice
from libraries.factories import FCMFactory
import numpy as np
import copy
from django.db import connection


def data_latih_index(request):
    return render(request, 'pemain_belakang/data-latih/index.html')



@csrf_exempt
def data_latih_detail(request):
    id_data_latih_belakang = request.POST.get('id')
    if (id_data_latih_belakang == None or id_data_latih_belakang == ''):
        context = context_response(False, 'id tidak boleh kosong')


    data_latih_belakang = DataLatihPemain.objects.get(pk=id_data_latih_belakang)
    serial = model_to_dict(data_latih_belakang)

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

    form = DataLatihBelakangForm(request.POST)
    if form.is_valid():
       post_data = form.cleaned_data
       data_latih_belakang = DataLatihPemain()
       data_latih_belakang.posisi = 2
       data_latih_belakang.nama = post_data['nama']
       data_latih_belakang.usia = post_data['usia']
       data_latih_belakang.pemain_inti = post_data['pemain_inti']
       data_latih_belakang.cadangan_main = post_data['cadangan_main']
       data_latih_belakang.mop = post_data['mop']
       data_latih_belakang.kk = post_data['kk']
       data_latih_belakang.km = post_data['km']
       data_latih_belakang.gol = post_data['gol']
       data_latih_belakang.assist = post_data['assist']
       data_latih_belakang.pelanggaran = post_data['pelanggaran']
       data_latih_belakang.dilanggar_lawan = post_data['dilanggar_lawan']
       data_latih_belakang.akurasi_tembakan = post_data['akurasi_tembakan']
       data_latih_belakang.akurasi_operan = post_data['akurasi_operan']
       data_latih_belakang.akurasi_umpan_silang = post_data['akurasi_umpan_silang']
       data_latih_belakang.sukses_tekel = post_data['sukses_tekel']

       data_latih_belakang.set_bobot_data()
       data_latih_belakang.save()

       context = context_response(True, 'sukses menambah data latih pemain belakang')

    else:
       context = context_response(False, form.errors)

    return context

@csrf_exempt
def data_latih_update(request):
    form = DataLatihBelakangForm(request.POST)

    if form.is_valid():
       post_data = form.cleaned_data
       data_latih_belakang = DataLatihPemain.objects.get(pk=request.POST.get('id'))
       data_latih_belakang.nama = post_data['nama']
       data_latih_belakang.usia = post_data['usia']
       data_latih_belakang.pemain_inti = post_data['pemain_inti']
       data_latih_belakang.cadangan_main = post_data['cadangan_main']
       data_latih_belakang.mop = post_data['mop']
       data_latih_belakang.kk = post_data['kk']
       data_latih_belakang.km = post_data['km']
       data_latih_belakang.gol = post_data['gol']
       data_latih_belakang.assist = post_data['assist']
       data_latih_belakang.pelanggaran = post_data['pelanggaran']
       data_latih_belakang.dilanggar_lawan = post_data['dilanggar_lawan']
       data_latih_belakang.akurasi_tembakan = post_data['akurasi_tembakan']
       data_latih_belakang.akurasi_operan = post_data['akurasi_operan']
       data_latih_belakang.akurasi_umpan_silang = post_data['akurasi_umpan_silang']
       data_latih_belakang.sukses_tekel = post_data['sukses_tekel']

       data_latih_belakang.set_bobot_data()
       data_latih_belakang.save()
       context = context_response(True, ['sukses merubah data latih pemain belakang'])

    else:
       context = context_response(False, form.errors)

    return context

@csrf_exempt
def data_latih_delete(request):
    id_data_latih_belakang = request.POST.get('id')
    data_latih_belakang = DataLatihPemain.objects.get(pk=id_data_latih_belakang)

    if (data_latih_belakang.delete()):
        context = context_response(True, 'sukses menghapus data latih')
    else:
        context = context_response(False, 'gagal menghapus data latih')

    return JsonResponse(context, safe=False)


@csrf_exempt
def data_latih_import(request):

    excel_file = request.FILES['excel_file']

    wb = openpyxl.load_workbook(excel_file)
    worksheet = wb['Sheet1']
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
       'assist',
       'pelanggaran',
       'dilanggar_lawan',
       'akurasi_tembakan',
       'akurasi_operan',
       'akurasi_umpan_silang',
       'sukses_tekel',
       ]

    for row in islice(worksheet.iter_rows(), 1, None):

       row_data = dict()
       for index in range(len(row)):
         row_data[field_names[index]] = str(row[index].value).strip()
         data_latih_belakang = DataLatihPemain(**row_data)
         data_latih_belakang.posisi = 2
         data_latih_belakang.set_bobot_data()
       excel_data.append(data_latih_belakang)



    if request.POST.get('hapus_seluruh_data') == 'on':
       DataLatihPemain.get_posisi_belakang().delete()

    DataLatihPemain.objects.bulk_create(excel_data)
    total_data = len(DataLatihPemain.get_posisi_belakang().values())
    context = context_response(True, {'total_data': total_data})
    return JsonResponse(context, safe=False)

#
# fungsi-fungsi terkait pengujian FCM
#
#
def pengujian_index(request):
    return render(request, 'pemain_belakang/pengujian/index.html')

@csrf_exempt
def pengujian_proses(request):
    jumlah_cluster = int(request.POST.get('jumlah_cluster'))
    max_iter = int(request.POST.get('max_iter'))
    max_error = float(request.POST.get('max_error'))

    data_latih_all_fields = DataLatihPemain.get_posisi_belakang()
    fields = ['id', 'nama', 'norm_usia', 'norm_pemain_inti', 'norm_cadangan_main', 'norm_mop', 'norm_kk', 'norm_km', 'norm_gol', 'norm_assist', 'norm_pelanggaran', 'norm_dilanggar_lawan', 'norm_akurasi_tembakan', 'norm_akurasi_operan', 'norm_akurasi_umpan_silang', 'norm_sukses_tekel']


    data_latih = list(data_latih_all_fields.values(*fields))

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
         'norm_assist',
         'norm_pelanggaran',
         'norm_dilanggar_lawan',
         'norm_akurasi_tembakan',
         'norm_akurasi_operan',
         'norm_akurasi_umpan_silang',
         'norm_sukses_tekel']

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



