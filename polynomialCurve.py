# gerekli kütüphaneleri ekliyoruz
import numpy as np # matematiksel islemler icin
import matplotlib.pyplot as plt # grafik çizimi için
import itertools # renk ve çizgi stilleri için

# kullanıcıdan veri toplama fonksiyonu 
# bu fonksiyon, kullanıcıdan bir değişken isimlerini (x ve y) ve bu değişken için veri alıyor.
# veri girişi sırasında, kullanıcı 'E' tuşuna basarak veri girişini sonlandırabilir.
def collect_data(variable_name):
    data = []
    print(f"Enter data for {variable_name}. Enter 'E' for end of data.")
    while True:
        value = input(f"{variable_name} value: ")
        if value.upper() == 'E':  # 'E' ile girişi sonlandırıcak
            break
        try:
            #excelde bazı dosyalarda nokta yerine virgül kullanıldığı için bu durumu düzeltmek için (yani sayı değilde metin gibi durduğu için)
            value = value.replace(',', '.')
            data.append(float(value))
        except ValueError:
            print("Please enter a valid number.")
    return np.array(data)

# renkler ve çizgi stilleri için itertools kütüphanesi kullandım 
colors = itertools.cycle(['r', 'g', 'b', 'm', 'c', 'y', 'k'])
line_styles = itertools.cycle(['-', '--', '-.', ':'])

# grafik oluşturma işlemi
plt.figure(figsize=(12, 10))

# ilk olarak x ve y ekseni isimlerini soruyor(veri isimlerini)
x_name = input("Enter the name of the x-axis data (e.g., 'Wind Speed'): ")
y_name = input("Enter the name of the y-axis data (e.g., 'Power Output'): ")

# grafik üzerinde birden fazla tribün görmek isteyen kullanıcılar için yeni tribün ekleme döngüsü
while True:
    # rüzgar tribünü ismi soruluyor
    wind_turbine_name = input("Enter the wind turbine name (e.g., 'Wind Turbine 1'): ")

    # verileri topluyor
    x = collect_data(x_name)
    y = collect_data(y_name)

    # x ve y uzunlukları kontrolü eşit değilse hata mesajı
    if len(x) != len(y):
        print("Error: The number of x and y values must be the same.")
        continue

    # trendline hesaplama (4. dereceden polinom)!!
    polynomial_coefficients = np.polyfit(x, y, 4)
    polynomial = np.poly1d(polynomial_coefficients)

    # grafik için x ekseninde çizim aralığını kullanıcı  verilerine göre ayarlıyor
    x_graph = np.linspace(min(x), max(x), 100)
    y_graph = polynomial(x_graph)

    # grafik üzerine oluşturulan trendline'ın çizim kısmı
    color = next(colors)
    line_style = next(line_styles)
    plt.plot(x_graph, y_graph, line_style, color=color, label=f'{wind_turbine_name}')

    # kullanıcıya başka bir rüzgar tribünü eklemek isteyip istemediğini soruyor
    another = input("Wanna add another wind turbine? (Y/N): ")
    if another.upper() != 'Y':
        break

# grafiğin ekranda gösterilmesi kısmı
plt.xlabel(x_name)
plt.ylabel(y_name)
plt.legend(loc='best')
plt.title("Wind Turbine Trendline Graph")
plt.show()






