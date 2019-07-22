from django.utils.translation import gettext_lazy as _

# Provincial code in Indonesia doesn't comply with the standard 3-letter province code
# data taken from the official page of Indonesian internal affair ministry
# http://www.kemendagri.go.id/pages/data-wilayah
PROVINCE_CHOICES = (
    ('ACEH', _('Nanggroe Aceh Darussalam')),
    ('BABEL', _('Kepulauan Bangka-Belitung')),
    ('BALI', _('Bali')),
    ('BANTEN', _('Banten')),
    ('BENGKULU', _('Bengkulu')),
    ('DI_YOGYAKARTA', _('DI Yogyakarta')),  # Special Region Yogyakarta
    ('DKI_JAKARTA', _('DKI Jakarta')),  # Special Capital Region Jakarta
    ('GORONTALO', _('Gorontalo')),
    ('JABAR', _('Jawa Barat')),
    ('JAMBI', _('Jambi')),
    ('JATENG', _('Jawa Tengah')),
    ('JATIM', _('Jawa Timur')),
    ('KALBAR', _('Kalimantan Barat')),
    ('KALSEL', _('Kalimantan Selatan')),
    ('KALTENG', _('Kalimantan Tengah')),
    ('KALTIM', _('Kalimantan Timur')),
    ('KALUT', _('Kalimantan Utara')),
    ('KEPRI', _('Kepulauan Riau')),
    ('LAMPUNG', _('Lampung')),
    ('MALUKU', _('Maluku')),
    ('MALUT', _('Maluku Utara')),
    ('NTB', _('Nusa Tenggara Barat')),
    ('NTT', _('Nusa Tenggara Timur')),
    ('PAPUA', _('Papua')),
    ('PAPUA_BARAT', _('Papua Barat')),
    ('RIAU', _('Riau')),
    ('SULBAR', _('Sulawesi Barat')),
    ('SULSEL', _('Sumatera Selatan')),
    ('SULTENG', _('Sulawesi Tengah')),
    ('SULTRA', _('Sulawesi Tenggara')),
    ('SULUT', _('Sulawesi Utara')),
    ('SUMBAR', _('Sumatera Barat')),
    ('SUMSEL', _('Sumatera Selatan')),
    ('SUMUT', _('Sumatera Utara')),
)

#: License plate prefixes
LICENSE_PLATE_PREFIX_CHOICES = (
    ('A', _('Banten')),
    ('AA', _('Magelang')),
    ('AB', _('Yogyakarta')),
    ('AD', _('Surakarta - Solo')),
    ('AE', _('Madiun')),
    ('AG', _('Kediri')),
    ('B', _('Jakarta')),
    ('BA', _('Sumatera Barat')),
    ('BB', _('Tapanuli')),
    ('BD', _('Bengkulu')),
    ('BE', _('Lampung')),
    ('BG', _('Sumatera Selatan')),
    ('BH', _('Jambi')),
    ('BK', _('Sumatera Utara')),
    ('BL', _('Nanggroe Aceh Darussalam')),
    ('BM', _('Riau')),
    ('BN', _('Kepulauan Bangka Belitung')),
    ('BP', _('Kepulauan Riau')),
    ('CC', _('Corps Consulate')),
    ('CD', _('Corps Diplomatic')),
    ('D', _('Bandung')),
    ('DA', _('Kalimantan Selatan')),
    ('DB', _('Sulawesi Utara Daratan')),
    ('DC', _('Sulawesi Barat')),
    ('DD', _('Sulawesi Selatan')),
    ('DE', _('Maluku')),
    ('DG', _('Maluku Utara')),
    ('DH', _('NTT - Timor')),
    ('DK', _('Bali')),
    ('DL', _('Sulawesi Utara Kepulauan')),
    ('DM', _('Gorontalo')),
    ('DN', _('Sulawesi Tengah')),
    ('DR', _('NTB - Lombok')),
    ('DS', _('Papua dan Papua Barat')),
    ('DT', _('Sulawesi Tenggara')),
    ('E', _('Cirebon')),
    ('EA', _('NTB - Sumbawa')),
    ('EB', _('NTT - Flores')),
    ('ED', _('NTT - Sumba')),
    ('F', _('Bogor')),
    ('G', _('Pekalongan')),
    ('H', _('Semarang')),
    ('K', _('Pati')),
    ('KB', _('Kalimantan Barat')),
    ('KH', _('Kalimantan Tengah')),
    ('KT', _('Kalimantan Timur')),
    ('L', _('Surabaya')),
    ('M', _('Madura')),
    ('N', _('Malang')),
    ('P', _('Jember')),
    ('R', _('Banyumas')),
    ('RI', _('Federal Government')),
    ('S', _('Bojonegoro')),
    ('T', _('Purwakarta')),
    ('W', _('Sidoarjo')),
    ('Z', _('Garut')),
)
