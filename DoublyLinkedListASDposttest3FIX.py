import os
import time
os.system("cls")

# ###### MENDEFINISIKAN KELAS PYTHON
class Contact:
    def __init__(self, nama, no_hp):
        self.nama = nama
        self.no_hp = no_hp
        self.next = None
        self.previous = None


# ###### MENDEFINISIKAN KELAS KONTAKLIST  
class ContactList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.history = []
    
#      ###### MENAMBAHKAN KONTAK   
    def add_contact(self):
        print("")
        os.system("cls")
        nama = input("MASUKKAN NAMA KONTAK: ")
        no_hp = input("MASUKKAN NOMOR TELEPON: ")

        no_baru = Contact(nama, no_hp)
        if self.head is None:
            self.head = no_baru
            self.tail = no_baru    
        else:
            no_baru.previous = self.tail
            self.tail.next = no_baru
            self.tail = no_baru
        self.history.append(("Kontak Ditambahkan", nama, no_hp))
        print("")
        print("=== KONTAK BERHASIL DITAMBAHKAN ===")
        print("Mohon Tunggu...")
        time.sleep(3)
        os.system("cls")
        
#     ###### MENGHAPUS KONTAK
    def delete_contact(self):
        print("")
        os.system("cls")
        nama = input("MASUKKAN NAMA KONTAK YANG INGIN DIHAPUS: ")
        current = self.head
        while current:
            if current.nama.lower() == nama.lower():
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None
                elif current == self.head:
                    self.head = current.next
                    current.next.previous = None
                elif current == self.tail:
                    self.tail = current.previous
                    current.previous.next = None
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                self.history.append(("Kontak Dihapus", current.nama, current.no_hp))
                print("")
                print("=== KONTAK BERHASIL DIHAPUS ===")
                print("Mohon Tunggu...")
                time.sleep(3)
                os.system("cls")
                return
            current = current.next
        print("")
        print("=== MAAF, KONTAK TIDAK DITEMUKAN ===")
    
    ###### MENAMPILKAN KONTAK
    def display_contacts(self, page_num=1, page_size=10):
        current = self.head
        count = 0
        start_index = (page_num - 1) * page_size
        end_index = start_index + page_size

        while current:
            count += 1
            if count > start_index and count <= end_index:
                print(str(count) + ".", current.nama, "-", current.no_hp)
            current = current.next
            if count == end_index:
                break
        total_pages = (count // page_size) + (1 if count % page_size != 0 else 0)
        print("")
        print("Halaman", str(page_num) + "/" + str(total_pages) + ", jumlah kontak:", count)
        print("====================================")
        print("Mohon Tunggu...")
        time.sleep(8)
        os.system("cls")
    
#     ###### MENCARI KONTAK
    def search_contact(self):
        print("")
        os.system("cls")
        nama = input("MASUKKAN NAMA KONTAK YANG INGIN DICARI: ")
        current = self.head
        result = []
        while current:
            if current.nama.lower().find(nama.lower()) != -1:
                result.append(current)
            current = current.next
        if len(result) == 0:
            print("")
            print("MAAF, TIDAK DITEMUKAN KONTAK DENGAN NAMA TERSEBUT")
        else:
            os.system("cls")
            print(">>>> HASIL PENCARIAN KONTAK <<<<")
            print("")
            for contact in result:
                print(contact.nama, "-", contact.no_hp)
                time.sleep(5)
                os.system("cls")
    
    ###### MENAMPILKAN RIWAYAT        
    def display_history(self):
        os.system("cls")
        print("============== RIWAYAT ANDA ===============".center(70))
        print("===========================================".center(70))
        print("")
        if len(self.history) == 0:
            print("MAAF, TIDAK ADA RIWAYAT ANDA".center(70))
        else:
            for action in self.history:
                print(action[0], "--->", action[1], "-", action[2])
                
# ###### MENU PROGRAM                
def main():
    print("")
    contact_list = ContactList()
    while True:
        print("============================================================".center(70))
        print("======== SILAHKAN PILIH MENU YANG INGIN ANDA AKSES =========".center(70))
        print("============================================================".center(70))
        print("""
        +====================================================+
        |           ==== MENU YANG TERSEDIA ====             |
        +====================================================+
        |                (1) TAMBAH KONTAK                   |
        |                (2) HAPUS KONTAK                    |
        |                (3) LIHAT KONTAK                    |
        |                (4) CARI KONTAK                     |
        |                (5) LIHAT HISTORY                   |
        |                (6) KEMBALI                         |
        +====================================================+
        """)
        print("")
        
        choice = input("SILAHKAN PILIH MENU YANG ANDA INGINKAN (1-6): ")

        if choice == '1':
            contact_list.add_contact()
        elif choice == '2':
            contact_list.delete_contact()
        elif choice == '3':
            os.system("cls")
            page_num = int(input("MAUKKAN NOMOR HALAMAN YANG INGIN DITAMPILKAN: "))
            page_size = int(input("MASUKKAN UKURAN HALAMAN YANG INGIN DITAMPILKAN: "))
            print("Mohon Tunggu...")
            time.sleep(3)
            os.system("cls")
            print("=======  DAFTAR KONTAK ANDA  =======")
            print("====================================")
            print("")
            contact_list.display_contacts(page_num, page_size)
        elif choice == '4':
            contact_list.search_contact()
        elif choice == '5':
            contact_list.display_history()
        elif choice == '6':
            break
        else:
            print("=== MAAF TIDAK ADA PILIHAN, SILAHKAN PILIH ULANG (1-6) ===")
            
###### MENJALANKAN PROGRAM
if __name__ == '__main__':
    main()
