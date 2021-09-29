s = input('Nhập vào 1 câu: ')
tu_dai_nhat = ''
ds_cac_tu = s.split()
for tu in ds_cac_tu:
    if (len(tu) > len(tu_dai_nhat)) or (len(tu) == len(tu_dai_nhat) and tu < tu_dai_nhat):
        tu_dai_nhat = tu
print(f'Từ dài nhất trong câu: {tu_dai_nhat}')