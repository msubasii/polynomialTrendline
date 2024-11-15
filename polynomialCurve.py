# Gerekli kütüphaneleri ekliyoruz
import numpy as np
import matplotlib.pyplot as plt
import itertools

# Kullanıcıdan veri toplama fonksiyonu
def collect_data(variable_name):
    data = []
    print(f"{variable_name} değerlerini girin (girişi bitirmek için 'E' yazın):")
    while True:
        value = input(f"{variable_name} değeri: ")
        if value.upper() == 'E':  # 'E' ile girişi sonlandır
            break
        try:
            value = value.replace(',', '.')
            data.append(float(value))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
    return np.array(data)

# Renkler ve çizgi stilleri için döngüleri oluşturmak için itertools kütüphanesini kullanıyoruz
colors = itertools.cycle(['r', 'g', 'b', 'm', 'c', 'y', 'k'])
line_styles = itertools.cycle(['-', '--', '-.', ':'])

# Grafik oluşturma işlemi
plt.figure(figsize=(10, 6))

# İlk olarak x ve y ekseni isimlerini soruyoruz
x_name = input("x ekseni verisi adını girin (örneğin, 'hız'): ")
y_name = input("y ekseni verisi adını girin (örneğin, 'MW'): ")

# Birden fazla rüzgar gülünün verilerini eklemek için döngü
while True:
    # Rüzgar gülü ismi soruluyor
    wind_turbine_name = input("Rüzgar gülünün adını girin (örneğin, 'Rüzgar Gülü 1'): ")

    # Verileri topluyoruz
    x = collect_data(x_name)
    y = collect_data(y_name)

    # x ve y uzunlukları kontrolü
    if len(x) != len(y):
        print("Hata: x ve y dizileri aynı uzunlukta olmalı.")
        continue

    # Trendline hesaplama (4. dereceden polinom)
    polynomial_coefficients = np.polyfit(x, y, 4)
    polynomial = np.poly1d(polynomial_coefficients)

    # Grafik için x ekseninde çizim aralığını belirliyoruz
    x_graph = np.linspace(min(x), max(x), 100)
    y_graph = polynomial(x_graph)

    # Grafik üzerine sadece trendline'ı çiziyoruz
    color = next(colors)
    line_style = next(line_styles)
    plt.plot(x_graph, y_graph, line_style, color=color, label=f'{wind_turbine_name}')

    # kullanıcıya başka bir rüzgar tribünü eklemek isteyip istemediğini soruyor
    another = input("Wanna add another wind turbine? (Y/N): ")
    if another.upper() != 'Y':
        break

# Grafik gösterimi
plt.xlabel(x_name)
plt.ylabel(y_name)
plt.legend(loc='best')
plt.title("Wind Turbine Trendline Graph")
plt.show()






