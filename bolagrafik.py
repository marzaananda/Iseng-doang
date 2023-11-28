import matplotlib.pyplot as plt

labels = ['Paskibra', 'Osis', 'SSI', 'PMR']
quantity = [5, 2, 4, 1]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

plt.title('Daftar Siswa Yang Masuk Organisasi Kelas XII IPA 1')
plt.pie(quantity, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')
plt.show()  # Call plt.show() as a function