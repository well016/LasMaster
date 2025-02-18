import numpy as np
import os
import lasio
from numpy.ma.core import min_val
from openpyxl import load_workbook
import pandas as pd


def get_analysis_collector():
    wells, well_names, well_horizons, well_range=data_reading()
    collector=[]
    for well,name,well_horizons,well_range in zip(wells,well_names,well_horizons,well_range):
        NML1=well['NML1']
        NML2=well['NML2']
        GK=well['GK']
        Sw=None
        gk_min = 0
        gk_max = 1
        diff_nml=1
        a3 = 1
        a4 = 2
        kgl = 1
        diff_1_2 = []

        for nml1, nml2 in zip(NML1, NML2):
            if nml1 != 0:
                diff = round((abs(nml1 - nml2) / nml1) * 100, 2)
            else:
                diff = 0  # или любое другое значение, если нужно
            diff_1_2.append(diff)

        ang = []
        lkgl = []
        for gk in GK:
            ag = round((gk - gk_min) / (gk_max - gk_min), 3)
            ang.append(ag)
        for i in ang:
            d = a3 * i ** a4
            lkgl.append(d)
        collector_status = []

        ''' 3 сигмы'''
        nonan_NML1 = NML1[~np.isnan(NML1)]  # удалил все NaN из списка
        I1 = sorted(nonan_NML1)[:len(nonan_NML1) // 20]  # отсортировал список и получил первые 5 % значений

        n = len(I1)  # количество элементов

        Icp = np.sum(I1) / n

        sigma = np.sqrt(np.sum((I1 - Icp) ** 2) / (n - 1))

        # print(sigma) # Результат 4.047381259858853

        ''''''

        for i, k ,nml1 in zip(diff_1_2, lkgl, NML1):
            #if i >= diff_nml and k < kgl and nml1 >  Icp + 3 * sigma:
            if i >= diff_nml and nml1 >  Icp + 3 * sigma:
                collector_status.append(1)
            else:
                collector_status.append(0)


        collector.append(collector_status)


    return collector




def data_reading():
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
                depth_sw=[]
                Sw=[]
                for row in sheet.iter_rows(min_row=2, max_col=4, values_only=True):
                    dep_sw = row[2]
                    if dep_sw is None:
                        continue
                    depth_sw.append(float(dep_sw))

                    s=row[3]
                    if s is None:
                        continue
                    Sw.append(float(s))

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
        common_depth=np.union1d(common_depth, depth_sw)
        Sw=np.interp(common_depth, depth_sw, Sw)
        GK = np.interp(common_depth, DEPTH_GK, GK)
        NML1_interp = np.interp(common_depth, DEPTH_NML, NML1)
        NML2_interp = np.interp(common_depth, DEPTH_NML, NML2)


        curves[k] = [{'GK': GK},
                     {'NML1': NML1_interp},
                     {'NML2': NML2_interp},
                     {'DEPTH': common_depth},
                     {'layer': [parsed_ranges, horizonts]},
                     {'Sw':Sw}]


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
    # if len(sorted_data) >= 5:
    #     d=len(sorted_data)//15 # 5% элементов скраю максимального
    #     fifth_from_end = sorted_data[-d]
    # else:
    #     fifth_from_end = None # Если меньше 5 элементов, возвращаем None
    #
    # max_val = fifth_from_end
    # Предпоследнее значение максимальное

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

            if curve.get('Sw') is not None:
                Sw = curve.get('Sw')

        if len(horizonts) == 0:
            continue
        depth_min = horizonts[0][0]
        depth_max = horizonts[0][1]
        u0 = np.round((NML1 ** (t2 / (t2 - t1))) / (NML2 ** (t1 / (t2 - t1))), 2)
        s = []
        # для нормализации по горизонту
        for i, j in zip(u0, DEPTH):
            if j >= depth_min and j <= depth_max:
                s.append(i)
            else:
                s.append(np.nan)

        norm = normalize(s)


        len_list=[]
        determ=[]
        count=[]
        for i in range(1,100,1):
            gk_min = 0
            gk_max = 1
            diff_nml = i
            a3 = 1
            a4 = 2
            kgl = 1
            diff_1_2 = []

            for nml1, nml2 in zip(NML1, NML2):
                if nml1 != 0:
                    diff = round((abs(nml1 - nml2) / nml1) * 100, 2)
                else:
                    diff = 0  # или любое другое значение, если нужно
                diff_1_2.append(diff)

            ang = []
            lkgl = []
            for gk in GK:
                ag = round((gk - gk_min) / (gk_max - gk_min), 3)
                ang.append(ag)
            for an in ang:
                d = a3 * an ** a4
                lkgl.append(d)
            collector_status = []

            ''' 3 сигмы'''
            nonan_NML1 = NML1[~np.isnan(NML1)]  # удалил все NaN из списка
            I1 = sorted(nonan_NML1)[:len(nonan_NML1) // 20]  # отсортировал список и получил первые 5 % значений

            n = len(I1)  # количество элементов

            Icp = np.sum(I1) / n

            sigma = np.sqrt(np.sum((I1 - Icp) ** 2) / (n - 1))

            # print(sigma) # Результат 4.047381259858853

            ''''''

            for dif, k, nml1 in zip(diff_1_2, lkgl, NML1):
                # if i >= diff_nml and k < kgl and nml1 >  Icp + 3 * sigma:
                if dif >= diff_nml and nml1 > Icp + 3 * sigma:
                    collector_status.append(1)
                else:
                    collector_status.append(0)

            intervals,stats =group_depths_by_status(collector_status,DEPTH,depth_min,depth_max)
            data = {
                "Интервал глубин,м": intervals,
                "Статус Коллектора": stats
            }
            df = pd.DataFrame(data)
            df = df[df['Статус Коллектора'] == 1]
            group_collector=df["Интервал глубин,м"].to_numpy()


            U0, SW = get_group_u0_sw(group_collector, DEPTH, Sw, norm)

            # Рассчитываем коэффициент корреляции
            ccorrelation_coefficient = np.corrcoef(U0, SW)[0, 1]

            # Коэффициент детерминации (R^2)
            r_squared = ccorrelation_coefficient  ** 2
            print(f"Коэффициент корреляции: {r_squared}, {i}, {len(U0)}")

            len_list.append(len(U0))
            count.append(i)
            determ.append(r_squared)
        out=pd.DataFrame({'Количество пропластков':len_list,'Коэффициент корреляции':determ,'Расхождение ямк':count})
        out.to_excel(f'{well}.xlsx')








def group_depths_by_status(collector,depths,depth_min,depth_max):
    intervals = []
    stats = []
    start_depth = depth_min
    statuses = collector
    current_status = statuses[0]

    for i in range(1, len(depths)):
        if depth_min <= depths[i - 1] <= depth_max:
            if statuses[i] != current_status:
                end_depth = depths[i - 1]
                if end_depth - start_depth >= 0.3:
                    intervals.append([start_depth,end_depth])
                    stats.append(current_status)
                start_depth = depths[i]
                current_status = statuses[i]

    end_depth = depth_max
    if end_depth - start_depth >= 0.3:
        intervals.append([start_depth,end_depth])
        stats.append(current_status)




    return intervals, stats


def get_group_u0_sw(parsed_ranges, DEPTH, Sw,norm):
    U0 = []
    SW = []

    for k in parsed_ranges:  # k 1135.1-1135.6
        result_u0 = []
        result_Sw = []
        depth_up, depth_down = k
        for i, j, s in zip(norm, DEPTH , Sw):
            if depth_up <= j <= depth_down:
                result_u0.append(i)
                result_Sw.append(s)

        max_val = max(result_u0)
        porog_max = max_val - 0 * max_val

        min_val = min(result_u0)
        porog_min = min_val + 0 * min_val

        result = [x for x in result_u0 if x <= porog_max and x >= porog_min]
        U0.append(sum(result) / len(result))
        SW.append(sum(result_Sw) / len(result_Sw))

    return U0, SW















get_u0()
