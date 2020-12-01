from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.datetime_safe import date
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Local_Authority(models.Model):
    authority_name = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
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

    WHITE_EUROPEAN = 'White European'
    DARK_EUROPEAN = 'Dark European'
    AFRO_CARIBBEAN = 'Afro Caribbean'
    ASIAN = 'Asian'
    ORIENTAL = 'Oriental'
    UNKNOWN = 'Unknown'

    ETHNICITY = [
        (WHITE_EUROPEAN, 'White European'),
        (DARK_EUROPEAN, 'Dark European'),
        (AFRO_CARIBBEAN, 'Afro Caribbean'),
        (ASIAN, 'Asian'),
        (ORIENTAL, 'Oriental'),
        (UNKNOWN, 'Unknown')
    ]

    yp_first_name = models.CharField(max_length=100)
    local_authority = models.ForeignKey(Local_Authority, on_delete=models.CASCADE)
    yp_assigned_id = models.CharField(max_length=100)
    yp_surname = models.CharField(max_length=100)
    yp_nickname = models.CharField(max_length=100)
    yp_gender = models.CharField(
        max_length=50,
        choices=GENDER_CHOICES,

    )
    yp_previous_name = models.CharField(max_length=100)
    yp_date_of_birth = models.DateField(default=date.today)
    yp_ethnicity = models.CharField(
        max_length=100,
        choices=ETHNICITY,
        default=WHITE_EUROPEAN,
    )
    yp_nationality = models.CharField(
        max_length=100,
        choices=COUNTRIES,
        default=UNITED_KINGDOM,
    )
    yp_country_origin = models.CharField(
        max_length=100,
        choices=COUNTRIES,
        default=UNITED_KINGDOM,
    )
    yp_first_language = models.CharField(
        max_length=50,
        choices=LANGUAGE,

    )
    yp_other_spoken_languages =models.CharField(
        max_length=50,
        choices=LANGUAGE,

    )
    yp_status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,

    )
    yp_uasc = models.CharField(
        max_length=10,
        choices=UASC_CHOICES,
        default=NO,
    )
    yp_date_added = models.DateTimeField(default=timezone.now)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Young Person General Information"

    def __str__(self):
        return self.yp_first_name + " - " + self.yp_surname

    def get_absolute_url(self):
        return reverse('child-detail', kwargs={'pk': self.pk})


class Profile(models.Model):
    yp = models.OneToOneField(YP_General_Information, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)