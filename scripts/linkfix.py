import json
import os
from os.path import join, dirname
from color import error, success, warning

# Dosya yollarını doğru ayarla
file = os.path.realpath(__file__)
base = dirname(dirname(file))
source = join(base, "source")
linkcheck_build = join(base, "build", "linkcheck")
output_file = join(linkcheck_build, "output.json")

# Çıktı dosyasını oku ve işle
try:
    with open(output_file, 'r', encoding='utf-8') as f:
        # Sphinx, her kırık link için birden fazla kayıt üretir.
        records = [json.loads(i) for i in f.readlines()]
except FileNotFoundError:
    error("ERROR: 'make linkcheck' komutunu çalıştırmalısınız.")
    exit()

warning("Eğer bir URL'yi değiştirirken hata yaparsanız, scripti sonlandırmak için CTRL + C'yi kullanabilirsiniz.\n")

cached_replacements = {}
replacements = []
broken = 0

# Linkleri işlemeye başla
for record in records:
    status = record['status']
    uri = record['uri']

    if status == "working":
        continue
    elif status == "unchecked":
        continue
    elif status == "redirected":
        # Yönlendirmenin kalıcı olup olmadığını kontrol et
        if record['code'] != 301:
            continue
        replace_with = record['info']
    elif status == "broken":
        try:
            replace_with = cached_replacements[uri]
        except KeyError:
            broken += 1
            print(f"Dosya: {record['filename']}")
            print(f"URL: {uri}")
            replace_with = input("Yukarıdaki URL kırık, yerine ne koymak istersiniz? Hiçbir şey yapmak istemiyorsanız boş bırakabilirsiniz.\n > ")
            
            if replace_with and not replace_with.isspace():
                success("Link değiştirildi.\n\n")
            else:
                warning("Geçiş yapılıyor.\n\n")
                continue
    elif status == "ignored":
        continue
    else:
        raise ValueError(f"Unknown status for URL {uri!r}: {status}")

    # :target: direktifine özel durum
    if replace_with == '.':
        continue

    replacements.append((record, replace_with))

# Değişiklikleri kontrol et
if broken == 0:
    success("Tüm bağlantılar güncel, kırık bağlantı yok.")
elif len(replacements) == 0:
    success(f"{broken} kırık linkten hiçbiri değiştirilmedi.")
else:
    warning("Yaptığınız değişikliklerden emin olduktan sonra Enter tuşuna basarak devam edin.")
    input()
    success(f"{broken} kırık linkten {len(replacements)}'i değiştirildi.")

# Dosya içeriğini güncelleme
for record, replacement in replacements:
    rst_file = join(source, record['filename'])
    uri = record['uri']

    try:
        with open(rst_file, 'r', encoding="utf-8") as f:
            data = f.read()
    except FileNotFoundError:
        warning(f"{rst_file} dosyası bulunamadı. Atlanıyor.\n")
        continue

    # URL'yi dosya içinde arama
    if uri not in data:
        alternative_uri = uri.split(":", 1)[0]
        if alternative_uri not in data:
            warning(f"UYARI: URL '{uri}' {rst_file} dosyasının içinde bulunamadı. Bu, ':target:' direktifi ile ilgili olabilir.\n")
            continue
        uri = alternative_uri

    # URL'yi değiştir
    data = data.replace(uri, replacement)

    # :target: direktifini özel olarak kontrol et
    if uri.startswith("_images") or uri.startswith("/images"):
        data = "\n".join([i for i in data.split("\n") if ":target:" not in i])

    try:
        with open(rst_file, 'w', encoding="utf-8") as f:
            f.write(data)
    except Exception as e:
        error(f"{rst_file} dosyasına yazılırken hata oluştu: {e}")

