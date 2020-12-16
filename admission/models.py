from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.datetime_safe import date
from django.conf import settings
from ckeditor.fields import RichTextField
from PIL import Image
# Create your models here.


class Local_Authority(models.Model):
    authority_name = models.CharField(max_length=100)
    authority_address = models.CharField(max_length=100)
    authority_address_2 = models.CharField(max_length=100)
    authority_location = models.CharField(max_length=100)
    authority_postcode = models.CharField(max_length=100)
    authority_email = models.CharField(max_length=100)
    authority_phone = models.IntegerField(default=0)
    authority_emergency_number = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Local Authority Information"

    def __str__(self):
        return self.authority_name

    def get_absolute_url(self):
        return reverse('authority-detail', kwargs={'pk': self.pk})


class Care_House_Information(models.Model):

    OPTION_1 = 'Detached'
    OPTION_2 = 'Semi-Detached'
    OPTION_3 = 'Terraced'
    OPTION_4 = 'End of Terrace'
    OPTION_5 = 'Flat'
    OPTION_6 = 'Studio Flat'
    OPTION_7 = 'Split-Level Flat'
    OPTION_8 = 'Converted Flat'
    OPTION_9 = 'Maisonette'
    OPTION_10 = 'Cottage'
    OPTION_11 = 'Bungalow'
    OPTION_12 = 'Mansion'

    OPTN_1 = 1
    OPTN_2 = 2
    OPTN_3 = 3
    OPTN_4 = 4
    OPTN_5 = 5
    OPTN_6 = 6
    OPTN_7 = 7
    OPTN_8 = 8
    OPTN_9 = 9
    OPTN_10 = 10
    OPTN_11 = 11
    OPTN_12 = 12

    PLACEMENT_CHOICES = [
        (OPTION_1, 'Detached'),
        (OPTION_2, 'Semi-Detached'),
        (OPTION_3, 'Terraced'),
        (OPTION_4, 'End of Terrace'),
        (OPTION_5, 'Flat'),
        (OPTION_6, 'Studio Flat'),
        (OPTION_7, 'Split-Level Flat'),
        (OPTION_8, 'Converted Flat'),
        (OPTION_9, 'Maisonette'),
        (OPTION_10, 'Cottage'),
        (OPTION_11, 'Bungalow'),
        (OPTION_12, 'Mansion'),

    ]

    NUMBER_CHOICES = [
        (OPTN_1, 1),
        (OPTN_2, 2),
        (OPTN_3, 3),
        (OPTN_4, 4),
        (OPTN_5, 5),
        (OPTN_6, 6),
        (OPTN_7, 7),
        (OPTN_8, 8),
        (OPTN_9, 9),
        (OPTN_10, 10),
        (OPTN_11, 11),
        (OPTN_12, 12),
    ]

    house_name = models.CharField(max_length=100)
    location_id = models.CharField(max_length=100)
    house_address_one = models.CharField(max_length=100)
    house_address_two = models.CharField(max_length=100, default='')
    postcode = models.CharField(max_length=100)
    house_number = models.IntegerField(default=0)
    house_email = models.EmailField(max_length=254, default='')
    number_of_beds = models.IntegerField(choices=NUMBER_CHOICES, default=OPTN_1)
    number_of_bathrooms = models.IntegerField(choices=NUMBER_CHOICES, default=OPTN_1)
    house_type_of_accommodation = models.CharField(max_length=50, choices=PLACEMENT_CHOICES)
    date_added = models.DateTimeField (default=timezone.now)

    class Meta:
        verbose_name_plural = "Care House Information"

    def __str__(self):
        return self.house_name

    def get_absolute_url(self):
        return reverse('home-detail', kwargs={'pk': self.pk})


class YP_General_Information(models.Model):
    # Boolean

    YES = 'Yes'
    NO = 'No'
    UASC_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),]

    # Gender

    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    # Status

    S17 = 'S17'
    S20 = 'S20'
    S21 = 'S21'
    S22 = 'S22'
    S24 = 'S24'
    S31 = 'S31'
    S33 = 'S33'
    S38 = 'S38'
    STATUS_CHOICES = [
        (S17, 'S17'),
        (S20, 'S20'),
        (S21, 'S21'),
        (S22, 'S22'),
        (S24, 'S24'),
        (S31, 'S31'),
        (S33, 'S33'),
        (S38, 'S38'),

    ]

    # Language
    MANDARIN = 'Mandarin'
    SPANISH = 'Spanish'
    ENGLISH = 'English'
    HINDI = 'Hindi'
    ARABIC = 'Arabic'
    PORTUGUESE = 'Portuguese'
    BENGALI = 'Bengali'
    RUSSIAN = 'Russian'
    JAPANESE = 'Japanese'
    PUNJABI = 'Punjabi'
    GERMAN = 'German'
    JAVANESE = 'Javanese'
    WU_INC_SHANGHAINESE = 'Wu (inc. Shanghainese)'
    MALAY_INDONESIAN = 'Malay/Indonesian'
    TELUGU = 'Telugu'
    VIETNAMESE = 'Vietnamese'
    KOREAN = 'Korean'
    FRENCH = 'French'
    MARATHI = 'Marathi'
    TAMIL = 'Tamil'
    URDU = 'Urdu'
    TURKISH = 'Turkish'
    ITALIAN = 'Italian'
    YUE_CANTONESE = 'Yue (Cantonese)'
    THAI = 'Thai'
    GUJARATI = 'Gujarati'
    JIN = 'Jin'
    SOUTHERN_MIN = 'Southern Min'
    PERSIAN = 'Persian'
    POLISH = 'Polish'
    PASHTO = 'Pashto'
    KANNADA = 'Kannada'
    XIANG_HUNNANESE = 'Xiang (Hunnanese)'
    MALAYALAM = 'Malayalam'
    SUNDANESE = 'Sundanese'
    HAUSA = 'Hausa'
    ODIA_ORIYA = 'Odia (Oriya)'
    BURMESE = 'Burmese'
    HAKKA = 'Hakka'
    UKRAINIAN = 'Ukrainian'
    BHOJPURI = 'Bhojpuri'
    TAGALOG = 'Tagalog'
    YORUBA = 'Yoruba'
    MAITHILI = 'Maithili'
    UZBEK = 'Uzbek'
    SINDHI = 'Sindhi'
    AMHARIC = 'Amharic'
    FULA = 'Fula'
    ROMANIAN = 'Romanian'
    OROMO = 'Oromo'
    IGBO = 'Igbo'
    AZERBAIJANI = 'Azerbaijani'
    AWADHI = 'Awadhi'
    GAN_CHINESE = 'Gan Chinese'
    CEBUANO_VISAYAN = 'Cebuano (Visayan)'
    DUTCH = 'Dutch'
    KURDISH = 'Kurdish'
    SERBO_CROATIAN = 'Serbo-Croatian'
    MALAGASY = 'Malagasy'
    SARAIKI = 'Saraiki'
    NEPALI = 'Nepali'
    SINHALESE = 'Sinhalese'
    CHITTAGONIAN = 'Chittagonian'
    ZHUANG = 'Zhuang'
    KHMER = 'Khmer'
    TURKMEN = 'Turkmen'
    ASSAMESE = 'Assamese'
    MADURESE = 'Madurese'
    SOMALI = 'Somali'
    MARWARI = 'Marwari'
    MAGAHI = 'Magahi'
    HARYANVI = 'Haryanvi'
    HUNGARIAN = 'Hungarian'
    CHHATTISGARHI = 'Chhattisgarhi'
    GREEK = 'Greek'
    CHEWA = 'Chewa'
    DECCAN = 'Deccan'
    AKAN = 'Akan'
    KAZAKH = 'Kazakh'
    NORTHERN_MIN = 'Northern Min'
    SYLHETI = 'Sylheti'
    ZULU = 'Zulu'
    CZECH = 'Czech'
    KINYARWANDA = 'Kinyarwanda'
    DHUNDHARI = 'Dhundhari'
    HAITIAN_CREOLE = 'Haitian Creole'
    EASTERN_MIN = 'Eastern Min'
    ILOCANO = 'Ilocano'
    QUECHUA = 'Quechua'
    KIRUNDI = 'Kirundi'
    SWEDISH = 'Swedish'
    HMONG = 'Hmong'
    SHONA = 'Shona'
    UYGHUR = 'Uyghur'
    HILIGAYNON = 'Hiligaynon'
    MOSSI = 'Mossi'
    XHOSA = 'Xhosa'
    BELARUSIAN = 'Belarusian'
    BALOCHI = 'Balochi'
    KONKANI = 'Konkani'

    LANGUAGE =[
        (MANDARIN, 'Mandarin'),
        (SPANISH, 'Spanish'),
        (ENGLISH, 'English'),
        (HINDI, 'Hindi'),
        (ARABIC, 'Arabic'),
        (PORTUGUESE, 'Portuguese'),
        (BENGALI, 'Bengali'),
        (RUSSIAN, 'Russian'),
        (JAPANESE, 'Japanese'),
        (PUNJABI, 'Punjabi'),
        (GERMAN, 'German'),
        (JAVANESE, 'Javanese'),
        (WU_INC_SHANGHAINESE, 'Wu (inc. Shanghainese)'),
        (MALAY_INDONESIAN, 'Malay/Indonesian'),
        (TELUGU, 'Telugu'),
        (VIETNAMESE, 'Vietnamese'),
        (KOREAN, 'Korean'),
        (FRENCH, 'French'),
        (MARATHI, 'Marathi'),
        (TAMIL, 'Tamil'),
        (URDU, 'Urdu'),
        (TURKISH, 'Turkish'),
        (ITALIAN, 'Italian'),
        (YUE_CANTONESE, 'Yue (Cantonese)'),
        (THAI, 'Thai'),
        (GUJARATI, 'Gujarati'),
        (JIN, 'Jin'),
        (SOUTHERN_MIN, 'Southern Min'),
        (PERSIAN, 'Persian'),
        (POLISH, 'Polish'),
        (PASHTO, 'Pashto'),
        (KANNADA, 'Kannada'),
        (XIANG_HUNNANESE, 'Xiang (Hunnanese)'),
        (MALAYALAM, 'Malayalam'),
        (SUNDANESE, 'Sundanese'),
        (HAUSA, 'Hausa'),
        (ODIA_ORIYA, 'Odia (Oriya)'),
        (BURMESE, 'Burmese'),
        (HAKKA, 'Hakka'),
        (UKRAINIAN, 'Ukrainian'),
        (BHOJPURI, 'Bhojpuri'),
        (TAGALOG, 'Tagalog'),
        (YORUBA, 'Yoruba'),
        (MAITHILI, 'Maithili'),
        (UZBEK, 'Uzbek'),
        (SINDHI, 'Sindhi'),
        (AMHARIC, 'Amharic'),
        (FULA, 'Fula'),
        (ROMANIAN, 'Romanian'),
        (OROMO, 'Oromo'),
        (IGBO, 'Igbo'),
        (AZERBAIJANI, 'Azerbaijani'),
        (AWADHI, 'Awadhi'),
        (GAN_CHINESE, 'Gan Chinese'),
        (CEBUANO_VISAYAN, 'Cebuano (Visayan)'),
        (DUTCH, 'Dutch'),
        (KURDISH, 'Kurdish'),
        (SERBO_CROATIAN, 'Serbo-Croatian'),
        (MALAGASY, 'Malagasy'),
        (SARAIKI, 'Saraiki'),
        (NEPALI, 'Nepali'),
        (SINHALESE, 'Sinhalese'),
        (CHITTAGONIAN, 'Chittagonian'),
        (ZHUANG, 'Zhuang'),
        (KHMER, 'Khmer'),
        (TURKMEN, 'Turkmen'),
        (ASSAMESE, 'Assamese'),
        (MADURESE, 'Madurese'),
        (SOMALI, 'Somali'),
        (MARWARI, 'Marwari'),
        (MAGAHI, 'Magahi'),
        (HARYANVI, 'Haryanvi'),
        (HUNGARIAN, 'Hungarian'),
        (CHHATTISGARHI, 'Chhattisgarhi'),
        (GREEK, 'Greek'),
        (CHEWA, 'Chewa'),
        (DECCAN, 'Deccan'),
        (AKAN, 'Akan'),
        (KAZAKH, 'Kazakh'),
        (NORTHERN_MIN, 'Northern Min'),
        (SYLHETI, 'Sylheti'),
        (ZULU, 'Zulu'),
        (CZECH, 'Czech'),
        (KINYARWANDA, 'Kinyarwanda'),
        (DHUNDHARI, 'Dhundhari'),
        (HAITIAN_CREOLE, 'Haitian Creole'),
        (EASTERN_MIN, 'Eastern Min'),
        (ILOCANO, 'Ilocano'),
        (QUECHUA, 'Quechua'),
        (KIRUNDI, 'Kirundi'),
        (SWEDISH, 'Swedish'),
        (HMONG, 'Hmong'),
        (SHONA, 'Shona'),
        (UYGHUR, 'Uyghur'),
        (HILIGAYNON, 'Hiligaynon'),
        (MOSSI, 'Mossi'),
        (XHOSA, 'Xhosa'),
        (BELARUSIAN, 'Belarusian'),
        (BALOCHI, 'Balochi'),
        (KONKANI, 'Konkani'),

    ]

    AFGHANISTAN = 'Afghanistan'
    ALBANIA = 'Albania'
    ALGERIA = 'Algeria'
    ANDORRA = 'Andorra'
    ANGOLA = 'Angola'
    ANTIGUA_AND_BARBUDA = 'Antigua and Barbuda'
    ARGENTINA = 'Argentina'
    ARMENIA = 'Armenia'
    AUSTRALIA = 'Australia'
    AUSTRIA = 'Austria'
    AZERBAIJAN = 'Azerbaijan'
    THE_BAHAMAS = 'The Bahamas'
    BAHRAIN = 'Bahrain'
    BANGLADESH = 'Bangladesh'
    BARBADOS = 'Barbados'
    BELARUS = 'Belarus'
    BELGIUM = 'Belgium'
    BELIZE = 'Belize'
    BENIN = 'Benin'
    BHUTAN = 'Bhutan'
    BOLIVIA = 'Bolivia'
    BOSNIA_AND_HERZEGOVINA = 'Bosnia and Herzegovina'
    BOTSWANA = 'Botswana'
    BRAZIL = 'Brazil'
    BRUNEI = 'Brunei'
    BULGARIA = 'Bulgaria'
    BURKINA_FASO = 'Burkina Faso'
    BURUNDI = 'Burundi'
    CAMBODIA = 'Cambodia'
    CAMEROON = 'Cameroon'
    CANADA = 'Canada'
    CAPE_VERDE = 'Cape Verde'
    CENTRAL_AFRICAN_REPUBLIC = 'Central African Republic'
    CHAD = 'Chad'
    CHILE = 'Chile'
    CHINA = 'China'
    COLOMBIA = 'Colombia'
    COMOROS = 'Comoros'
    CONGO_REPUBLIC = 'Congo, Republic '
    CONGO_DEMOCRATIC_REPUBLIC = 'Congo, Democratic Republic'
    COSTA_RICA = 'Costa Rica'
    COTE_D_IVOIRE = 'Cote D Ivoire'
    CROATIA = 'Croatia'
    CUBA = 'Cuba'
    CYPRUS = 'Cyprus'
    CZECH_REPUBLIC = 'Czech Republic'
    DENMARK = 'Denmark'
    DJIBOUTI = 'Djibouti'
    DOMINICA = 'Dominica'
    DOMINICAN_REPUBLIC = 'Dominican Republic'
    EAST_TIMOR = 'East Timor (Timor-Leste)'
    ECUADOR = 'Ecuador'
    EGYPT = 'Egypt'
    EL_SALVADOR = 'El Salvador'
    EQUATORIAL_GUINEA = 'Equatorial Guinea'
    ERITREA = 'Eritrea'
    ESTONIA = 'Estonia'
    ETHIOPIA = 'Ethiopia'
    FIJI = 'Fiji'
    FINLAND = 'Finland'
    FRANCE = 'France'
    GABON = 'Gabon'
    THE_GAMBIA = 'The Gambia'
    GEORGIA = 'Georgia'
    GERMANY = 'Germany'
    GHANA = 'Ghana'
    GREECE = 'Greece'
    GRENADA = 'Grenada'
    GUATEMALA = 'Guatemala'
    GUINEA = 'Guinea'
    GUINEA_BISSAU = 'Guinea-Bissau'
    GUYANA = 'Guyana'
    HAITI = 'Haiti'
    HONDURAS = 'Honduras'
    HUNGARY = 'Hungary'
    ICELAND = 'Iceland'
    INDIA = 'India'
    INDONESIA = 'Indonesia'
    IRAN = 'Iran'
    IRAQ = 'Iraq'
    IRELAND = 'Ireland'
    ISRAEL = 'Israel'
    ITALY = 'Italy'
    JAMAICA = 'Jamaica'
    JAPAN = 'Japan'
    JORDAN = 'Jordan'
    KAZAKHSTAN = 'Kazakhstan'
    KENYA = 'Kenya'
    KIRIBATI = 'Kiribati'
    KOREA_NORTH = 'Korea, North'
    KOREA_SOUTH = 'Korea, South'
    KOSOVO = 'Kosovo'
    KUWAIT = 'Kuwait'
    KYRGYZSTAN = 'Kyrgyzstan'
    LAOS = 'Laos'
    LATVIA = 'Latvia'
    LEBANON = 'Lebanon'
    LESOTHO = 'Lesotho'
    LIBERIA = 'Liberia'
    LIBYA = 'Libya'
    LIECHTENSTEIN = 'Liechtenstein'
    LITHUANIA = 'Lithuania'
    LUXEMBOURG = 'Luxembourg'
    MACEDONIA = 'Macedonia'
    MADAGASCAR = 'Madagascar'
    MALAWI = 'Malawi'
    MALAYSIA = 'Malaysia'
    MALDIVES = 'Maldives'
    MALI = 'Mali'
    MALTA = 'Malta'
    MARSHALL_ISLANDS = 'Marshall Islands'
    MAURITANIA = 'Mauritania'
    MAURITIUS = 'Mauritius'
    MEXICO = 'Mexico'
    MICRONESIA = 'Micronesia'
    MOLDOVA = 'Moldova'
    MONACO = 'Monaco'
    MONGOLIA = 'Mongolia'
    MONTENEGRO = 'Montenegro'
    MOROCCO = 'Morocco'
    MOZAMBIQUE = 'Mozambique'
    MYANMAR = 'Myanmar (Burma)'
    NAMIBIA = 'Namibia'
    NAURU = 'Nauru'
    NEPAL = 'Nepal'
    NETHERLANDS = 'Netherlands'
    NEW_ZEALAND = 'New Zealand'
    NICARAGUA = 'Nicaragua'
    NIGER = 'Niger'
    NIGERIA = 'Nigeria'
    NORWAY = 'Norway'
    OMAN = 'Oman'
    PAKISTAN = 'Pakistan'
    PALAU = 'Palau'
    PANAMA = 'Panama'
    PAPUA_NEW_GUINEA = 'Papua New Guinea'
    PARAGUAY = 'Paraguay'
    PERU = 'Peru'
    PHILIPPINES = 'Philippines'
    POLAND = 'Poland'
    PORTUGAL = 'Portugal'
    QATAR = 'Qatar'
    ROMANIA = 'Romania'
    RUSSIA = 'Russia'
    RWANDA = 'Rwanda'
    SAINTKITTS_AND_NEVIS = 'Saint Kitts and Nevis'
    SAINT_LUCIA = 'Saint Lucia'
    SAINT_VINCENT_AND_THE_GRENADINES = 'Saint Vincent and the Grenadines'
    SAMOA = 'Samoa'
    SAN_MARINO = 'San Marino'
    SAO_TOME_AND_PRINCIPE = 'Sao Tome and Principe'
    SAUDI_ARABIA = 'Saudi Arabia'
    SENEGAL = 'Senegal'
    SERBIA = 'Serbia'
    SEYCHELLES = 'Seychelles'
    SIERRA_LEONE = 'Sierra Leone'
    SINGAPORE = 'Singapore'
    SLOVAKIA = 'Slovakia'
    SLOVENIA = 'Slovenia'
    SOLOMON_ISLANDS = 'Solomon Islands'
    SOMALIA = 'Somalia'
    SOUTH_AFRICA = 'South Africa'
    SOUTH_SUDAN = 'South Sudan'
    SPAIN = 'Spain'
    SRI_LANKA = 'Sri Lanka'
    SUDAN = 'Sudan'
    SURINAME = 'Suriname'
    SWAZILAND = 'Swaziland'
    SWEDEN = 'Sweden'
    SWITZERLAND = 'Switzerland'
    SYRIA = 'Syria'
    TAIWAN = 'Taiwan'
    TAJIKISTAN = 'Tajikistan'
    TANZANIA = 'Tanzania'
    THAILAND = 'Thailand'
    TOGO = 'Togo'
    TONGA = 'Tonga'
    TRINIDAD_AND_TOBAGO = 'Trinidad and Tobago'
    TUNISIA = 'Tunisia'
    TURKEY = 'Turkey'
    TURKMENISTAN = 'Turkmenistan'
    TUVALU = 'Tuvalu'
    UGANDA = 'Uganda'
    UKRAINE = 'Ukraine'
    UNITED_ARAB_EMIRATES = 'United Arab Emirates'
    UNITED_KINGDOM = 'United Kingdom'
    UNITED_STATES_OF_AMERICA = 'United States of America'
    URUGUAY = 'Uruguay'
    UZBEKISTAN = 'Uzbekistan'
    VANUATU = 'Vanuatu'
    VATICAN_CITY = 'Vatican City'
    VENEZUELA = 'Venezuela'
    VIETNAM = 'Vietnam'
    YEMEN = 'Yemen'
    ZAMBIA = 'Zambia'
    ZIMBABWE = 'Zimbabwe'

    COUNTRIES = [
        (AFGHANISTAN, 'Afghanistan'),
        (ALBANIA, 'Albania'),
        (ALGERIA, 'Algeria'),
        (ANDORRA, 'Andorra'),
        (ANGOLA, 'Angola'),
        (ANTIGUA_AND_BARBUDA, 'Antigua and Barbuda'),
        (ARGENTINA, 'Argentina'),
        (ARMENIA, 'Armenia'),
        (AUSTRALIA, 'Australia'),
        (AUSTRIA, 'Austria'),
        (AZERBAIJAN, 'Azerbaijan'),
        (THE_BAHAMAS, 'The Bahamas'),
        (BAHRAIN, 'Bahrain'),
        (BANGLADESH, 'Bangladesh'),
        (BARBADOS, 'Barbados'),
        (BELARUS, 'Belarus'),
        (BELGIUM, 'Belgium'),
        (BELIZE, 'Belize'),
        (BENIN, 'Benin'),
        (BHUTAN, 'Bhutan'),
        (BOLIVIA, 'Bolivia'),
        (BOSNIA_AND_HERZEGOVINA, 'Bosnia and Herzegovina'),
        (BOTSWANA, 'Botswana'),
        (BRAZIL, 'Brazil'),
        (BRUNEI, 'Brunei'),
        (BULGARIA, 'Bulgaria'),
        (BURKINA_FASO, 'Burkina Faso'),
        (BURUNDI, 'Burundi'),
        (CAMBODIA, 'Cambodia'),
        (CAMEROON, 'Cameroon'),
        (CANADA, 'Canada'),
        (CAPE_VERDE, 'Cape Verde'),
        (CENTRAL_AFRICAN_REPUBLIC, 'Central African Republic'),
        (CHAD, 'Chad'),
        (CHILE, 'Chile'),
        (CHINA, 'China'),
        (COLOMBIA, 'Colombia'),
        (COMOROS, 'Comoros'),
        (CONGO_REPUBLIC, 'Congo, Republic '),
        (CONGO_DEMOCRATIC_REPUBLIC, 'Congo, Democratic Republic'),
        (COSTA_RICA, 'Costa Rica'),
        (COTE_D_IVOIRE, 'Cote D Ivoire'),
        (CROATIA, 'Croatia'),
        (CUBA, 'Cuba'),
        (CYPRUS, 'Cyprus'),
        (CZECH_REPUBLIC, 'Czech Republic'),
        (DENMARK, 'Denmark'),
        (DJIBOUTI, 'Djibouti'),
        (DOMINICA, 'Dominica'),
        (DOMINICAN_REPUBLIC, 'Dominican Republic'),
        (EAST_TIMOR, 'East Timor (Timor-Leste)'),
        (ECUADOR, 'Ecuador'),
        (EGYPT, 'Egypt'),
        (EL_SALVADOR, 'El Salvador'),
        (EQUATORIAL_GUINEA, 'Equatorial Guinea'),
        (ERITREA, 'Eritrea'),
        (ESTONIA, 'Estonia'),
        (ETHIOPIA, 'Ethiopia'),
        (FIJI, 'Fiji'),
        (FINLAND, 'Finland'),
        (FRANCE, 'France'),
        (GABON, 'Gabon'),
        (THE_GAMBIA, 'The Gambia'),
        (GEORGIA, 'Georgia'),
        (GERMANY, 'Germany'),
        (GHANA, 'Ghana'),
        (GREECE, 'Greece'),
        (GRENADA, 'Grenada'),
        (GUATEMALA, 'Guatemala'),
        (GUINEA, 'Guinea'),
        (GUINEA_BISSAU, 'Guinea-Bissau'),
        (GUYANA, 'Guyana'),
        (HAITI, 'Haiti'),
        (HONDURAS, 'Honduras'),
        (HUNGARY, 'Hungary'),
        (ICELAND, 'Iceland'),
        (INDIA, 'India'),
        (INDONESIA, 'Indonesia'),
        (IRAN, 'Iran'),
        (IRAQ, 'Iraq'),
        (IRELAND, 'Ireland'),
        (ISRAEL, 'Israel'),
        (ITALY, 'Italy'),
        (JAMAICA, 'Jamaica'),
        (JAPAN, 'Japan'),
        (JORDAN, 'Jordan'),
        (KAZAKHSTAN, 'Kazakhstan'),
        (KENYA, 'Kenya'),
        (KIRIBATI, 'Kiribati'),
        (KOREA_NORTH, 'Korea, North'),
        (KOREA_SOUTH, 'Korea, South'),
        (KOSOVO, 'Kosovo'),
        (KUWAIT, 'Kuwait'),
        (KYRGYZSTAN, 'Kyrgyzstan'),
        (LAOS, 'Laos'),
        (LATVIA, 'Latvia'),
        (LEBANON, 'Lebanon'),
        (LESOTHO, 'Lesotho'),
        (LIBERIA, 'Liberia'),
        (LIBYA, 'Libya'),
        (LIECHTENSTEIN, 'Liechtenstein'),
        (LITHUANIA, 'Lithuania'),
        (LUXEMBOURG, 'Luxembourg'),
        (MACEDONIA, 'Macedonia'),
        (MADAGASCAR, 'Madagascar'),
        (MALAWI, 'Malawi'),
        (MALAYSIA, 'Malaysia'),
        (MALDIVES, 'Maldives'),
        (MALI, 'Mali'),
        (MALTA, 'Malta'),
        (MARSHALL_ISLANDS, 'Marshall Islands'),
        (MAURITANIA, 'Mauritania'),
        (MAURITIUS, 'Mauritius'),
        (MEXICO, 'Mexico'),
        (MICRONESIA, 'Micronesia'),
        (MOLDOVA, 'Moldova'),
        (MONACO, 'Monaco'),
        (MONGOLIA, 'Mongolia'),
        (MONTENEGRO, 'Montenegro'),
        (MOROCCO, 'Morocco'),
        (MOZAMBIQUE, 'Mozambique'),
        (MYANMAR, 'Myanmar (Burma)'),
        (NAMIBIA, 'Namibia'),
        (NAURU, 'Nauru'),
        (NEPAL, 'Nepal'),
        (NETHERLANDS, 'Netherlands'),
        (NEW_ZEALAND, 'New Zealand'),
        (NICARAGUA, 'Nicaragua'),
        (NIGER, 'Niger'),
        (NIGERIA, 'Nigeria'),
        (NORWAY, 'Norway'),
        (OMAN, 'Oman'),
        (PAKISTAN, 'Pakistan'),
        (PALAU, 'Palau'),
        (PANAMA, 'Panama'),
        (PAPUA_NEW_GUINEA, 'Papua New Guinea'),
        (PARAGUAY, 'Paraguay'),
        (PERU, 'Peru'),
        (PHILIPPINES, 'Philippines'),
        (POLAND, 'Poland'),
        (PORTUGAL, 'Portugal'),
        (QATAR, 'Qatar'),
        (ROMANIA, 'Romania'),
        (RUSSIA, 'Russia'),
        (RWANDA, 'Rwanda'),
        (SAINTKITTS_AND_NEVIS, 'Saint Kitts and Nevis'),
        (SAINT_LUCIA, 'Saint Lucia'),
        (SAINT_VINCENT_AND_THE_GRENADINES, 'Saint Vincent and the Grenadines'),
        (SAMOA, 'Samoa'),
        (SAN_MARINO, 'San Marino'),
        (SAO_TOME_AND_PRINCIPE, 'Sao Tome and Principe'),
        (SAUDI_ARABIA, 'Saudi Arabia'),
        (SENEGAL, 'Senegal'),
        (SERBIA, 'Serbia'),
        (SEYCHELLES, 'Seychelles'),
        (SIERRA_LEONE, 'Sierra Leone'),
        (SINGAPORE, 'Singapore'),
        (SLOVAKIA, 'Slovakia'),
        (SLOVENIA, 'Slovenia'),
        (SOLOMON_ISLANDS, 'Solomon Islands'),
        (SOMALIA, 'Somalia'),
        (SOUTH_AFRICA, 'South Africa'),
        (SOUTH_SUDAN, 'South Sudan'),
        (SPAIN, 'Spain'),
        (SRI_LANKA, 'Sri Lanka'),
        (SUDAN, 'Sudan'),
        (SURINAME, 'Suriname'),
        (SWAZILAND, 'Swaziland'),
        (SWEDEN, 'Sweden'),
        (SWITZERLAND, 'Switzerland'),
        (SYRIA, 'Syria'),
        (TAIWAN, 'Taiwan'),
        (TAJIKISTAN, 'Tajikistan'),
        (TANZANIA, 'Tanzania'),
        (THAILAND, 'Thailand'),
        (TOGO, 'Togo'),
        (TONGA, 'Tonga'),
        (TRINIDAD_AND_TOBAGO, 'Trinidad and Tobago'),
        (TUNISIA, 'Tunisia'),
        (TURKEY, 'Turkey'),
        (TURKMENISTAN, 'Turkmenistan'),
        (TUVALU, 'Tuvalu'),
        (UGANDA, 'Uganda'),
        (UKRAINE, 'Ukraine'),
        (UNITED_ARAB_EMIRATES, 'United Arab Emirates'),
        (UNITED_KINGDOM, 'United Kingdom'),
        (UNITED_STATES_OF_AMERICA, 'United States of America'),
        (URUGUAY, 'Uruguay'),
        (UZBEKISTAN, 'Uzbekistan'),
        (VANUATU, 'Vanuatu'),
        (VATICAN_CITY, 'Vatican City'),
        (VENEZUELA, 'Venezuela'),
        (VIETNAM, 'Vietnam'),
        (YEMEN, 'Yemen'),
        (ZAMBIA, 'Zambia'),
        (ZIMBABWE, 'Zimbabwe'),

    ]

    OPTION_1 = 'White - English/Welsh/Scottish/Northern Irish/British'
    OPTION_2 = 'White - Irish'
    OPTION_3 = 'White - Gypsy or Irish Traveller'
    OPTION_4 = 'White - Any other White background'
    OPTION_5 = 'Mixed - White and Black Caribbean'
    OPTION_6 = 'Mixed - White and Black African'
    OPTION_7 = 'Mixed - White and Asian'
    OPTION_8 = 'Mixed - Any other Mixed/Multiple ethnic background'
    OPTION_9 = 'Asian - Indian'
    OPTION_10 = 'Asian - Pakistani'
    OPTION_11 = 'Asian - Bangladeshi'
    OPTION_12 = 'Asian - Chinese'
    OPTION_13 = 'Asian - Any other Asian background'
    OPTION_14 = 'Black - African'
    OPTION_15 = 'Black - Caribbean'
    OPTION_16 = 'Black - Any other Black/African/Caribbean background'
    OPTION_17 = 'Arab'
    OPTION_18 = 'Any other ethnic group'

    ETHNICITY = [
        (OPTION_1, 'White - English/Welsh/Scottish/Northern Irish/British'),
        (OPTION_2, 'White - Irish'),
        (OPTION_3, 'White - Gypsy or Irish Traveller'),
        (OPTION_4, 'White - Any other White background'),
        (OPTION_5, 'Mixed - White and Black Caribbean'),
        (OPTION_6, 'Mixed - White and Black African'),
        (OPTION_7, 'Mixed - White and Asian'),
        (OPTION_8, 'Mixed - Any other Mixed/Multiple ethnic background'),
        (OPTION_9, 'Asian - Indian'),
        (OPTION_10, 'Asian - Pakistani'),
        (OPTION_11, 'Asian - Bangladeshi'),
        (OPTION_12, 'Asian - Chinese'),
        (OPTION_13, 'Asian - Any other Asian background'),
        (OPTION_14, 'Black - African'),
        (OPTION_15, 'Black - Caribbean'),
        (OPTION_16, 'Black - Any other Black/African/Caribbean background'),
        (OPTION_17, 'Arab'),
        (OPTION_18, 'Any other ethnic group'),

    ]

    STAT_1 = 'Young Parent'
    STAT_2 = 'Not a Parent'

    STAT_CHOICES = [
        (STAT_1, 'Young Parent'),
        (STAT_2, 'Not a Parent'),

    ]

    yp_first_name = models.CharField(max_length=100)
    local_authority = models.ForeignKey(Local_Authority, on_delete=models.CASCADE)
    yp_assigned_id = models.CharField(max_length=100)
    yp_surname = models.CharField(max_length=100)
    yp_nickname = models.CharField(max_length=100)
    yp_gender = models.CharField(max_length=50, choices=GENDER_CHOICES,)
    yp_previous_name = models.CharField(max_length=100)
    yp_date_of_birth = models.DateField(default=date.today)
    yp_ethnicity = models.CharField(max_length=100, choices=ETHNICITY, default=OPTION_1)
    yp_nationality = models.CharField( max_length=100, choices=COUNTRIES, default=UNITED_KINGDOM)
    yp_country_origin = models.CharField( max_length=100, choices=COUNTRIES, default=UNITED_KINGDOM)
    yp_first_language = models.CharField( max_length=50, choices=LANGUAGE)
    yp_other_spoken_languages = models.CharField( max_length=50, choices=LANGUAGE,)
    yp_status = models.CharField(max_length=50, choices=STATUS_CHOICES,)
    yp_uasc = models.CharField(max_length=10, choices=UASC_CHOICES, default=NO,)
    yp_date_added = models.DateTimeField(default=timezone.now)
    parenthood = models.CharField(max_length=15, choices=STAT_CHOICES, default=NO,)
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assigned_home = models.ForeignKey(Care_House_Information, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Young Person General Information"

    def __str__(self):
        return self.yp_first_name + " - " + self.yp_surname

    def get_absolute_url(self):
        return reverse('child-detail', kwargs={'pk': self.pk})


class Profile_Pic(models.Model):
    yp = models.OneToOneField(YP_General_Information, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.yp} Young Person Profile Pic'

    def save(self, *args, **kwargs):
        super(Profile_Pic, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('child-detail', kwargs={'pk': self.pk})


class YP_Contact_Info(models.Model):
    YES = 'Yes'
    NO = 'No'
    BOOLEAN_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No'),

    ]

    yp = models.OneToOneField(YP_General_Information, on_delete=models.CASCADE)
    mobile_number = models.IntegerField(default=0)
    travel_card = models.CharField(
        max_length=10,
        choices=BOOLEAN_CHOICES,
        default=NO,
    )
    email_address = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    snapchat = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    other = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Young Person Contact Information"

    def __str__(self):
        return f'{self.yp}'

    def save(self, *args, **kwargs):
        super(YP_Contact_Info, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})


class YP_Health_And_Wellness (models.Model):
    yp = models.OneToOneField(YP_General_Information, on_delete=models.CASCADE)
    yp_ability_to_make_attachments = RichTextField(blank=True, null=True)
    yp_food_allergies = RichTextField(blank=True, null=True)
    yp_allergies_and_attitudes = RichTextField(blank=True, null=True)
    yp_resilience_and_self_esteem = RichTextField(blank=True, null=True)
    yp_substance_misuse_issues = RichTextField(blank=True, null=True)
    yp_sexual_health = RichTextField(blank=True, null=True)
    yp_Attitude_To_Food_And_Weight = RichTextField(blank=True, null=True)
    yp_smoking = RichTextField(blank=True, null=True)
    yp_personal_hygiene = RichTextField(blank=True, null=True)
    yp_learning_difficulties = RichTextField(blank=True, null=True)
    yp_physical_or_sensory_impairments_and_disabilities = RichTextField(blank=True, null=True)
    yp_healthcare_professional_involvement = RichTextField(blank=True, null=True)
    yp_date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Young Person Health and Wellness"

    def __str__(self):
        return f'{self.yp} Health and Wellness'

    def save(self, *args, **kwargs):
        super(YP_Health_And_Wellness, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('health-detail', kwargs={'pk': self.pk})


# Updates that need to be worked on

class YP_Banking_Information (models.Model):
    yp = models.OneToOneField(YP_General_Information, on_delete=models.CASCADE)
    yp_bank = models.CharField(max_length=100)
    yp_bank_name = models.CharField(max_length=100)
    yp_bank_sort_code = models.IntegerField(default=0)
    yp_bank_account_number = models.IntegerField(default=0)
    yp_date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Young Person Banking Information"

    def __str__(self):
        return f'{self.yp} Banking Details'

    def save(self, *args, **kwargs):
        super(YP_Banking_Information, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('bank-detail', kwargs={'pk': self.pk})


class YP_Physical_Description(models.Model):

    FAT = 'Fat'
    STOCKY = 'Stocky'
    PROP = 'Prop'
    THIN = 'Thin'
    SLIGHT = 'Slight'
    HEAVY = 'Heavy'
    BROAD = 'Broad'
    MEDIUM = 'Medium'
    SLIM = 'Slim'
    SMALL = 'Small'

    BUILD = [
        (FAT, 'Fat'),
        (STOCKY, 'Stocky'),
        (PROP, 'Prop'),
        (THIN, 'Thin'),
        (SLIGHT, 'Slight'),
        (HEAVY, 'Heavy'),
        (BROAD, 'Broad'),
        (MEDIUM, 'Medium'),
        (SLIM, 'Slim'),
        (SMALL, 'Small'),

    ]

    yp = models.OneToOneField(YP_General_Information, on_delete=models.CASCADE)
    yp_height = models.IntegerField(default=0)
    yp_weight = models.IntegerField(default=0)
    yp_build = models.CharField(
        max_length=10,
        choices=BUILD,
        default=SLIM,
    )
    yp_complexion = models.CharField(max_length=100)
    yp_eye_colour = models.CharField(max_length=100)
    yp_hair_colour = models.CharField(max_length=100)
    yp_marks_scars_tattoos = models.CharField(max_length=100)
    yp_disabilities = models.CharField(max_length=100)
    yp_relevant_medical_information = RichTextField(blank=True, null=True)
    yp_medications = RichTextField(blank=True, null=True)
    yp_date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Young Person Physical Description"

    def __str__(self):
        return f'{self.yp} Physical Description'

    def get_absolute_url(self):
        return reverse('physical-detail', kwargs={'pk': self.pk})


class YP_IPA (models.Model):
    yp = models.ForeignKey(YP_General_Information, related_name="ipa", on_delete=models.CASCADE)
    yp_placement_start_date = models.DateField(default=date.today)
    yp_initial_ipa_received_date = models.DateField(default=date.today)
    yp_last_ipa_start_date = models.DateField(default=date.today)
    yp_proposed_placement_end_date = models.DateField(default=date.today)
    yp_type_placement = models.CharField(max_length=100)
    yp_date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Young Person IPA"

    def __str__(self):
        return f'{self.yp} IPA Information'

    def save(self, *args, **kwargs):
        super(YP_IPA, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ipa-list', kwargs={'pk': self.pk})


class YP_Pen_Pic(models.Model):
    yp = models.OneToOneField(YP_General_Information, on_delete=models.CASCADE)
    yp_pen_picture = RichTextField(blank=True, null=True)
    yp_pen_picture_background = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Young Person Pen Picture"

    def __str__(self):
        return f'{self.yp}'

    def save(self, *args, **kwargs):
        super(YP_Pen_Pic, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pen-detail', kwargs={'pk': self.pk})


class YP_Profile_Child (models.Model):
    yp = models.OneToOneField(YP_General_Information, on_delete=models.CASCADE)
    yp_streghts = RichTextField(blank=True, null=True)
    yp_achivements = RichTextField(blank=True, null=True)
    yp_hobbies = RichTextField(blank=True, null=True)
    personality = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Young Person Contact Information"

    def __str__(self):
        return f'{self.yp}'

    def save(self, *args, **kwargs):
        super(YP_Profile_Child, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk': self.pk})


class YP_Relationships_Associates(models.Model):
    yp = models.ForeignKey(YP_General_Information, on_delete=models.CASCADE)
    next_of_kin = models.CharField(max_length=100)
    relationship_wth_next_kin = models.CharField(max_length=100)
    next_of_kin_phone = models.IntegerField(default=0)
    close_friend_name = models.CharField(max_length=100)
    contact_phone_close_friend = models.IntegerField(default=0)
    work_school_contact_phone = models.IntegerField(default=0)
    place_worship_details = RichTextField(blank=True, null=True)
    places_known_frequent = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Young Person Relationships and Associates"

    def __str__(self):
        return f'{self.yp}'

    def save(self, *args, **kwargs):
        super(YP_Relationships_Associates, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('relations-detail', kwargs={'pk': self.pk})