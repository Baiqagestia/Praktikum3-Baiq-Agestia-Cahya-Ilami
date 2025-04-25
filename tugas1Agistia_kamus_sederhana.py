# Program Kamus Sederhana
# Dibuat dengan profesional untuk memenuhi tugas mata kuliah

def main():
    # Membuat dictionary untuk kamus
    kamus = {
        "pisang": "buah berwarna kuning",
        "apel": "buah berwarna merah atau hijau",
        "jeruk": "buah berwarna oranye",
        "anggur": "buah kecil berwarna ungu atau hijau",
        "semangka": "buah besar dengan kulit hijau dan daging merah",
        "melon": "buah berwarna hijau muda dan rasanya manis",
        "pepaya": "buah lonjong dengan daging berwarna oranye",
        "nanas": "buah berduri di kulitnya dan berwarna kuning di dalam",
        "stroberi": "buah kecil berwarna merah dan rasanya asam manis",
        "durian": "buah beraroma kuat dan berkulit berduri",
        "mangga": "buah manis berwarna hijau atau kuning",
        "kelapa": "buah dengan air yang menyegarkan",
        "lemon": "buah kecil berwarna kuning dan rasanya asam",
        "alpukat": "buah hijau dengan tekstur lembut di dalam",
        "rambutan": "buah dengan rambut di kulitnya dan rasa manis"
    }

    print("=== Program Kamus Sederhana Baiq Agestia ===")
    kata = input("Masukkan kata(buah) yang ingin dicari artinya: ").lower()

    # Mencari arti kata
    arti = kamus.get(kata)
    
    if arti:
        print("="*80)
        print(f"Arti dari '{kata}' adalah: {arti}")
        print("="*80)
    else:
        print("="*80)
        print(f"Maaf, kata '{kata}' tidak ditemukan dalam kamus.")
        print("="*80)

if __name__ == "__main__":
    main()
