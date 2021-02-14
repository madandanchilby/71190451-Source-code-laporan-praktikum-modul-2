#chilby madandan/71190451
#soal Budi tertarik untuk melamar pekerjaan pada liburan semester yang akan berlangsung selama 5 minggu. Gaji yang diberikan adalah gaji per jam. Total pajak yang harus budi
#bayarkan dari penghasilannya selama bekerja adalah 14%. Setelah membayar pajak, budi
#menghabiskan 10% dari pendapatan bersihnya untuk membeli baju dan aksesoris yang akan
#digunakan pada semester baru, dan 1% untuk membeli alat tulis. Setelah membeli baju, aksesoris dan alat tulis, 
# Budi menggunakan 25% dari sisa uangnya untuk disedekahkan. Setiap
#Rp.1000 yang Budi sedekahkan 30% nya akan diserahkan kepada anak yatim, dan sisanya akan
#diserahkan ke kaum dhuafa.


waktu_kerja= 5 #minggu
pajak=14 #%
baju=10 #%
alat_tulis=1 #%
sedekah=25 #%
anak_yatim=30 #%
gaji=int(input('gaji per jam='))
jam_kerja=int(input('jumlah jam kerja dalam 1 minggu='))

pendapatan_Budi_sebelum_membayar_pajak=waktu_kerja * jam_kerja * gaji

penghasilan_bersih=pendapatan_Budi_sebelum_membayar_pajak * 0.14
bayar_pajak= round (penghasilan_bersih,2)
pendapatan_budi_setelah_membayar_pajak=pendapatan_Budi_sebelum_membayar_pajak-bayar_pajak
jumlah_uang_1=pendapatan_budi_setelah_membayar_pajak * 0.1
jumlah_uang_2=pendapatan_budi_setelah_membayar_pajak* 0.01
sisa_uang=pendapatan_budi_setelah_membayar_pajak-(jumlah_uang_1+jumlah_uang_2)
jumlah_uang_3=sisa_uang * 0.25
jumlah_uang_4=jumlah_uang_3 * 0.3
jumlah_uang_5=jumlah_uang_3 - jumlah_uang_4


print('pendapatan Budi sebelum membayar pajak=',pendapatan_Budi_sebelum_membayar_pajak)
print('Jumlah pajak yang harus dibayar=',bayar_pajak)
print('pendapatan budi setelah membayar pajak=',pendapatan_budi_setelah_membayar_pajak)
print('jumlah uang untuk membeli pakaian=',jumlah_uang_1)
print('jumlah uang untuk membeli alat tulis=',jumlah_uang_2)
print('sisa uang budi=',sisa_uang)
print('jumlah uang sedekah=',jumlah_uang_3)
print('jumlah uang yang di terima anak yatim=',jumlah_uang_4)
print('jumlah uang yang diterima kaum dhuafa=',jumlah_uang_5)