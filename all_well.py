import numpy as np
import os
import lasio
from openpyxl import load_workbook


def data_reading():
    global DEPTH_NML
    wells = {}
    curves = {}
    for root, dirs, files in os.walk('LAS'):
        for file in files:
            if file.endswith('.las'):
                well = os.path.join(root, file)  # путь к файлу
                folder_name = os.path.basename(root)  # название папки
                wells[folder_name] = wells.get(folder_name, []) + [well]
            elif file.endswith('depth.xlsx'):
                well = os.path.join(root, file)  # путь к файлу
                folder_name = os.path.basename(root)  # название папки
                wells[folder_name] = wells.get(folder_name, []) + [well]
    for k, v in wells.items():
        for i in v:

            if i.endswith('.las'):
                las = lasio.read(i)
                if 'NML1' in las.keys():
                    NML1 = las['NML1']
                    NML2 = las['NML2']
                    DEPTH_NML = las[0]

                if 'GK' in las.keys():
                    GK = las['GK']
                    DEPTH_GK = las[0]

            if i.endswith('depth.xlsx'):
                wb = load_workbook(i)
                sheet = wb.active
                parsed_ranges = []  # [(1135.08, 1136.83), (1137.09, 1137.36), ...]
                horizonts = []
                for row in sheet.iter_rows(min_row=2, max_col=2, values_only=True):
                    layer = row[0]  # строка вида для пропластка '1135,08-1136,83'
                    if layer is None:
                        continue
                    start_str, end_str = layer.split('-')
                    start_val = float(start_str.replace(',', '.'))
                    end_val = float(end_str.replace(',', '.'))
                    parsed_ranges.append([start_val, end_val])
                    horizont = row[1]  # строка вида для горизонта'1135,08-1136,83'
                    if horizont is None:
                        continue
                    start_str, end_str = horizont.split('-')
                    start_val = float(start_str.replace(',', '.'))
                    end_val = float(end_str.replace(',', '.'))
                    horizonts.append([start_val, end_val])

        common_depth = np.union1d(DEPTH_GK, DEPTH_NML)
        NML1_interp = np.interp(common_depth, DEPTH_NML, NML1)
        NML2_interp = np.interp(common_depth, DEPTH_NML, NML2)

        curves[k] = [{'GK': GK}, {'NML1': NML1_interp}, {'NML2': NML2_interp}, {'DEPTH': common_depth},
                     {'layer': [parsed_ranges, horizonts]}]
    return curves

# Нормализация надо менять
def normalize(data):
    data = np.array(data)  # Преобразуем в массив NumPy, если это еще не сделано
    # Применяем нормализацию, игнорируя NaN значения
    min_val = np.nanmin(data)  # Находим минимальное значение, игнорируя NaN
    max_val = np.nanmax(data)  # Находим максимальное значение, игнорируя NaN

    # Сортируем массив, игнорируя NaN
    sorted_data = np.sort(data[~np.isnan(data)])  # Убираем NaN и сортируем

    # Берём 5-е с конца значение
    if len(sorted_data) >= 5:
        d=len(sorted_data)//15 # 5% элементов
        fifth_from_end = sorted_data[-d]
    else:
        fifth_from_end = None  # Если меньше 5 элементов, возвращаем None

    max_val = fifth_from_end


    # Возвращаем нормализованные данные и 5-е с конца значение

    return (data - min_val) / (max_val - min_val)


def get_u0():
    t1 = 100
    t2 = 200
    curves = data_reading()  # Получаем данные

    # Проходим по всем скважинам и их данным
    for well, curve_list in curves.items():
        print(f"Обработка данных для скважины: {well}")
        for curve in curve_list:

            if curve.get('GK') is not None:
                GK = curve.get('GK')

            if curve.get('NML1') is not None:
                NML1 = curve.get('NML1')

            if curve.get('NML2') is not None:
                NML2 = curve.get('NML2')

            if curve.get('layer') is not None:
                parsed_ranges, horizonts = curve.get('layer')

            if curve.get('DEPTH') is not None:
                DEPTH = curve.get('DEPTH')

        if len(horizonts) == 0:
            continue
        depth_min = horizonts[0][0]
        depth_max = horizonts[0][1]
        u0 = np.round((NML1 ** (t2 / (t2 - t1))) / (NML2 ** (t1 / (t2 - t1))), 2)
        s = []
        for i, j in zip(u0, DEPTH):
            if j >= depth_min and j <= depth_max:
                s.append(i)
            else:
                s.append(np.nan)
        norm = normalize(s)
        for k in parsed_ranges:
            result = []
            depth_up, depth_down = k
            for i, j in zip(norm, DEPTH):
                if depth_up <= j <= depth_down:
                    result.append(i)
            max_val = max(result)
            threshold = max_val - 0.2* max_val
            result = [x for x in result if x <= threshold]
            print(str(sum(result) / len(result)).replace('.', ','))


get_u0()
