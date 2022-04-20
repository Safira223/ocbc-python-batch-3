# function untuk konversi suhu dari C -> K dan K -> C
def CK(temp,var):
    if var == 'K':
        result = temp + 273.15
    elif var == 'C':
        result = temp - 273.15
    print('Hasil Konversi Suhu : {} {}'.format(result,var))
    
# function untuk konversi suhu dari K/C ke F
def CK_to_F(temp,var):
    if var == 'C':
        result = 9/5 * temp + 32
    elif var == 'K':
        result = 9/5 * (temp-273.15) + 32
    print('Hasil Konversi Suhu : {} {}'.format(result,var))

# function untuk konversi suhu dari F ke C/K
def F_to_CK(temp,var):
    if var == 'C':
        result = (5/9) * temp -32
    elif var == 'K':
        result = (5/9) * (temp-32) + 273.15
    print('Hasil Konversi : {}{}'.format(result,var))
    
# function menu pilihan
def show_menu():
    
    print("============ Assignment 2 ============\n") 
    print("Hafizah Safira Kaurani (FSDO003ONL001)\n") 
    print("======================================\n") 

    menu = 0

    while True:
        print('\nProgram Konversi Suhu (Celcius, Kelvin,Fahrenheit)\n')
        print('1. Konversi suhu (C ke K) & (K ke C)\n')
        print('2. Konversi suhu ke F dari (C atau K)\n')
        print('3. Konversi Suhu dari F ke (C atau K)\n')
        print('4. Exit\n')

        # input menu yang dipilih
        menu = int(input('Pilih menu : '))

        if menu == 1:
            temp = int(input("Masukkan besar suhu : "))
            var = str(input("Pilih konversi suhu (C/K):"))
            # memanggil fungsi konversi suhu dari C -> K dan K -> C
            CK(temp,var)  
            continue

        elif menu == 2:
            temp = int(input("Masukkan besar suhu : "))
            var = str(input("Pilih konversi suhu (C/K):"))
            # memanggil fungsi konversi suhu dari K/C ke F
            CK_to_F(temp,var)
            continue

        elif menu == 3:
            temp = int(input("Masukkan Jumlah suhu(Fahrenheit) : "))
            var = str(input("Pilih konversi suhu (C/K):"))
            # memanggil fungsi konversi suhu dari F ke C/K
            F_to_CK(temp,var)
            continue

        elif menu == 4:
            # membuat pilihan exit
            pilih=str(input("Yakin ingin keluar? (y/n) "))
            # kembali ke menu pilihan jika batal exit
            if(pilih!='y'):
                show_menu()
            # keluar dari program 
            elif(pilih=='y'):
                print('Terima kasih..')
            break
        else:
            # apabila salah input pilihan menu
            print('Tidak ada pilihan tersebut, silahkan coba lagi\n')
            continue

# Memanggil function menu
if __name__=='__main__':
    show_menu()